from flask import Blueprint, request, Response
from twilio.twiml.voice_response import VoiceResponse
from datetime import datetime
from services.voice_processor import process_initial_call, process_gathered_input

twilio_bp = Blueprint('twilio_bp', __name__)


@twilio_bp.route('/incoming', methods=['POST'])
def incoming_call():
    """
    Handles an incoming call, initializes session metadata, and prompts the caller for input.
    """
    call_sid = request.form.get('CallSid', 'UNKNOWN_SID')
    caller_number = request.form.get('From', 'UNKNOWN_CALLER')
    called_number = request.form.get('To', 'UNKNOWN_RECEIVER')

    process_initial_call(call_sid, caller_number, called_number)

    response = VoiceResponse()
    response.say("Hello, thanks for calling Jivus AI! Please say something after the beep.")

    response.gather(input="speech", action="/twilio/gather", method="POST", speechTimeout="auto")

    response.say("We did not receive any input. Goodbye!")
    response.hangup()

    return Response(str(response), mimetype='text/xml')


@twilio_bp.route('/gather', methods=['POST'])
def gather_response():
    """
    Processes gathered speech input and generates an AI response.
    """
    caller_input = request.form.get('SpeechResult', '').strip()

    if not caller_input:
        response = VoiceResponse()
        response.say("We didn't catch that. Goodbye!")
        response.hangup()
        return Response(str(response), mimetype='text/xml')

    process_gathered_input(caller_input, datetime.now())

    response = VoiceResponse()

    audio_url = "https://8755-2401-4900-1c8e-83ab-b0b9-7f2c-5f18-29e0.ngrok-free.app/static/agent_response.mp3"
    response.play(audio_url)

    gather = response.gather(input="speech", action="/twilio/gather", method="POST", timeout=5, speechTimeout="auto")
    gather.say("Please say something after the beep.")

    return Response(str(response), mimetype='text/xml')
