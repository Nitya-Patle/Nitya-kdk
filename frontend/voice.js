function startVoice(){

const recognition = new webkitSpeechRecognition()

recognition.lang = "en-US"

recognition.onresult = function(event){

let voiceText = event.results[0][0].transcript

document.getElementById("message").value = voiceText

}

recognition.start()

}