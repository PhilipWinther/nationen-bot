function random_jokeprogramming() {
var baseURL = "https://v2.jokeapi.dev/";
var categories = ["Programming"];
var params = [
    "blacklistFlags=nsfw,racist,sexist",
    "idRange=0-304"
];


var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL + "/joke/" + categories.join(",") + "?" + params.join("&"));

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        if(randomJoke.type == "single")
        {
            // If type == "single", the joke only has the "joke" property
              document.getElementById("singleprogram").innerHTML = (randomJoke.joke);
                document.getElementById("setupprogram").innerHTML = ("");
           document.getElementById("deliveryprogram").innerHTML = ("");
           programspeak = (randomJoke.joke);
           programspeak1 = ("");
        }
        else
        {
            // If type == "single", the joke only has the "joke" property
               document.getElementById("setupprogram").innerHTML = (randomJoke.setup);
           document.getElementById("deliveryprogram").innerHTML = (randomJoke.delivery);
                 document.getElementById("singleprogram").innerHTML = ("");
                 programspeak = (randomJoke.setup)
                 programspeak1 = (randomJoke.delivery)
        }
    }
    else if(xhr.readyState == 4)
    {
        alert("Error while requesting joke.\n\nStatus code: " + xhr.status + "\nServer response: " + xhr.responseText);
    }
};

xhr.send();
}

function textToSpeechprogram() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-GB"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = programspeak + programspeak1;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
        
}


function random_jokemis() {
var baseURL = "https://v2.jokeapi.dev/";
var categories = ["Miscellaneous"];
var params = [
    "blacklistFlags=nsfw,racist,sexist",
    "idRange=0-304"
];

var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL + "/joke/" + categories.join(",") + "?" + params.join("&"));

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        if(randomJoke.type == "single")
        {
            // If type == "single", the joke only has the "joke" property
              document.getElementById("singlemis").innerHTML = (randomJoke.joke);
                document.getElementById("setupmis").innerHTML = ("");
                 document.getElementById("deliverymis").innerHTML = ("");
                 misspeak = (randomJoke.joke);
                 misspeak1 = ("");
        }
        else
        {
            // If type == "single", the joke only has the "joke" property
               document.getElementById("setupmis").innerHTML = (randomJoke.setup);
                document.getElementById("deliverymis").innerHTML = (randomJoke.delivery);
                document.getElementById("singlemis").innerHTML = ("");
                misspeak = (randomJoke.setup)
                misspeak1 = (randomJoke.delivery)
        }
    }
    else if(xhr.readyState == 4)
    {
        alert("Error while requesting joke.\n\nStatus code: " + xhr.status + "\nServer response: " + xhr.responseText);
    }
};

xhr.send();
}

function texttospeachmis() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-US"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = misspeak + misspeak1;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
}


function random_jokechucknorris() {
var baseURL = "https://api.chucknorris.io/jokes/random";

var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL);

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        document.getElementById("chuck-norris-test").innerHTML = (randomJoke.value);
        a = (randomJoke.value);

    }
};

xhr.send();
}



function texttospeachchucknorris() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-US"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = a;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
}


function random_jokechristmas() {
var baseURL = "https://v2.jokeapi.dev/";
var categories = ["Christmas"];
var params = [
    "blacklistFlags=nsfw,racist,sexist",
    "idRange=0-304"
];

var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL + "/joke/" + categories.join(",") + "?" + params.join("&"));

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        if(randomJoke.type == "single")
        {
            // If type == "single", the joke only has the "joke" property
              document.getElementById("singlechristmas").innerHTML = (randomJoke.joke);
                document.getElementById("setupchristmas").innerHTML = ("");
                 document.getElementById("deliverychristmas").innerHTML = ("");
                 christmasspeak = (randomJoke.joke);
                 christmasspeak1 = ("");
        }
        else
        {
            // If type == "single", the joke only has the "joke" property
               document.getElementById("setupchristmas").innerHTML = (randomJoke.setup);
                document.getElementById("deliverychristmas").innerHTML = (randomJoke.delivery);
                document.getElementById("singlechristmas").innerHTML = ("");
                christmasspeak = (randomJoke.setup)
                christmasspeak1 = (randomJoke.delivery)
        }
    }
    else if(xhr.readyState == 4)
    {
        alert("Error while requesting joke.\n\nStatus code: " + xhr.status + "\nServer response: " + xhr.responseText);
    }
};

xhr.send();
}


function texttospeachchristmas() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-US"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = christmasspeak + christmasspeak1;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
}


function random_jokepun() {
var baseURL = "https://v2.jokeapi.dev/";
var categories = ["pun"];
var params = [
    "blacklistFlags=nsfw,racist,sexist",
    "idRange=0-304"
];

var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL + "/joke/" + categories.join(",") + "?" + params.join("&"));

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        if(randomJoke.type == "single")
        {
            // If type == "single", the joke only has the "joke" property
              document.getElementById("singlepun").innerHTML = (randomJoke.joke);
                document.getElementById("setuppun").innerHTML = ("");
                 document.getElementById("deliverypun").innerHTML = ("");
                 punspeak = (randomJoke.joke);
                 punspeak1 = ("");
        }
        else
        {
            // If type == "single", the joke only has the "joke" property
               document.getElementById("setuppun").innerHTML = (randomJoke.setup);
                document.getElementById("deliverypun").innerHTML = (randomJoke.delivery);
                document.getElementById("singlepun").innerHTML = ("");
                punspeak = (randomJoke.setup)
                punspeak1 = (randomJoke.delivery)
        }
    }
    else if(xhr.readyState == 4)
    {
        alert("Error while requesting joke.\n\nStatus code: " + xhr.status + "\nServer response: " + xhr.responseText);
    }
};

xhr.send();
}


function texttospeachpun() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-US"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = punspeak + punspeak1;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
}

function random_jokespooky() {
var baseURL = "https://v2.jokeapi.dev/";
var categories = ["Spooky"];
var params = [
    "blacklistFlags=nsfw,racist,sexist",
    "idRange=0-304"
];

var xhr = new XMLHttpRequest();
xhr.open("GET", baseURL + "/joke/" + categories.join(",") + "?" + params.join("&"));

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status < 300) // readyState 4 means request has finished + we only want to parse the joke if the request was successful (status code lower than 300)
    {
        var randomJoke = JSON.parse(xhr.responseText);

        if(randomJoke.type == "single")
        {
            // If type == "single", the joke only has the "joke" property
              document.getElementById("singlespooky").innerHTML = (randomJoke.joke);
                document.getElementById("setupspooky").innerHTML = ("");
                 document.getElementById("deliveryspooky").innerHTML = ("");
                 spookyspeak = (randomJoke.joke);
                 spookyspeak1 = ("");
        }
        else
        {
            // If type == "single", the joke only has the "joke" property
               document.getElementById("setupspooky").innerHTML = (randomJoke.setup);
                document.getElementById("deliveryspooky").innerHTML = (randomJoke.delivery);
                document.getElementById("singlespooky").innerHTML = ("");
                spookyspeak = (randomJoke.setup)
                spookyspeak1 = (randomJoke.delivery)
        }
    }
    else if(xhr.readyState == 4)
    {
        alert("Error while requesting joke.\n\nStatus code: " + xhr.status + "\nServer response: " + xhr.responseText);
    }
};

xhr.send();
}



function texttospeachspooky() {
        // get all voices that browser offers
        var available_voices = window.speechSynthesis.getVoices();

        // this will hold an english voice
        var english_voice = '';

        // find voice by language locale "en-US"
        // if not then select the first voice
        for(var i=0; i<available_voices.length; i++) {
                if(available_voices[i].lang === 'en-GB') {
                        english_voice = available_voices[i];
                        break;
                }
        }
        if(english_voice === '')
                english_voice = available_voices[0];

        // new SpeechSynthesisUtterance object
        var utter = new SpeechSynthesisUtterance();
        utter.rate = 1;
        utter.pitch = 0.5;
        utter.text = spookyspeak + spookyspeak1;
        utter.voice = english_voice;

        // event after text has been spoken
        utter.onend = function() {
                alert('The joke has finished');
        };

        // speak
        window.speechSynthesis.speak(utter);
}


document.addEventListener('DOMContentLoaded', function () {

  document.getElementById('random_jokeprogrammingbutton')
    .addEventListener('click', random_jokeprogramming);


  document.getElementById('texttospeachprogrambutton')
    .addEventListener('click', textToSpeechprogram);


  document.getElementById('random_jokemisbutton')
    .addEventListener('click', random_jokemis);

  document.getElementById('texttospeachmisbutton')
    .addEventListener('click', texttospeachmis);

  document.getElementById('random_jokechucknorrisbutton')
    .addEventListener('click', random_jokechucknorris);

    document.getElementById('texttospeachchucknorrisbutton')
    .addEventListener('click', texttospeachchucknorris);

  document.getElementById('random_jokechristmasbutton')
    .addEventListener('click', random_jokechristmas);

  document.getElementById('texttospeachchristmasbutton')
    .addEventListener('click', texttospeachchristmas);

  document.getElementById('random_jokepunbutton')
    .addEventListener('click', random_jokepun);

 document.getElementById('texttospeachpunbutton')
    .addEventListener('click', texttospeachpun);

  document.getElementById('random_jokespookybutton')
    .addEventListener('click', random_jokespooky);

 document.getElementById('texttospeachspookybutton')
    .addEventListener('click', texttospeachspooky);


});


