import simplejson
import urllib
import urllib2
# url = "https://www.virustotal.com/vtapi/v2/comments/put"
# url = "https://www.virustotal.com/vtapi/v2/file/rescan"
url = "https://www.virustotal.com/vtapi/v2/file/report"
parameters = {"resource": "170b7a32adfc2b3ebbfe6bd4bb7d6acb3d0ed03e8d6945ab123e69eea893baee",
              "comment": "How to disinfect you from this file... #disinfect #zbot",
              "apikey": "a264d77db499762fa7de5cf0372c2129a288ff38e02a81e8a4a736ec3667f214"}
data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json = response.read()
# print json.positives
response_dict = simplejson.loads(json)
print response_dict.get("positives", {})
