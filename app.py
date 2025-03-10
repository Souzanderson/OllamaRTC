import json
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription
import aiohttp_cors
from chat import chat_assistent, set_personality
from time import sleep
import datetime

pcs = set()
channels = set()

async def index(request):
    return web.Response(text="Servidor WebRTC DataChannel rodando", content_type="text/plain")

def send_to_channels(channels, data, sender):
    try:
        for ch in channels:
            data_with_sender = {**data, "sender": sender}
            ch.send(json.dumps(data_with_sender, ensure_ascii=False))
    except Exception as e:
        print(f"[ERROR] Error:  => ", e)

async def set_personality(request):
    params = await request.json()
    personality = params["personality"]
    set_personality(personality)

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)

    @pc.on("datachannel")
    def on_datachannel(channel):
        print("DataChannel recebido:", channel.label)
        channels.add(channel)
        
        @channel.on("close")
        def on_close():
            print("Canal fechado:", channel.label)
            channels.discard(channel)

        @channel.on("message")
        def on_message(message):
            try:
                data = json.loads(message)
                print(channel.label, " => recebido => ", data)
                 # Reenviar para todos os canais ativos
                for ch in channels:
                    if ch != channel and ch.readyState == "open":  # Evita eco para o mesmo canal
                        data_with_sender = {**data, "sender": channel.label}
                        ch.send(json.dumps(data_with_sender, ensure_ascii=False))
                sleep(1)
                response_chat = chat_assistent(data["message"], data["user"])
                for ch in channels:
                    ch.send(json.dumps({
                            "message": response_chat,
                            "timestamp": datetime.datetime.now().isoformat(),
                            "user": "Tama"
                        }, ensure_ascii=False))
            except json.JSONDecodeError:
                print("Mensagem recebida (não-JSON):", message)
                
            except Exception as e:
                print(f"[ERROR] Error:  => ", e)

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.json_response({
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    })

app = web.Application()
app.router.add_get("/", index)
app.router.add_post("/offer", offer)
app.router.add_post("/personality", set_personality)

# Configure CORS
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

# Apply CORS to all routes
for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=8080)