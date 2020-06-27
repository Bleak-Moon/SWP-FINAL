from cgi import parse_qs
import matplotlib as mpl
mpl.use("Agg")
import mathplotlib.pyplot as plt
from template import html

def application(environ, start_response):
	d=parse_qs(environ["QUERY_STRING"])
	a=d.get("a", [""])[0]
	b=d.get("b", [""])[0]
	sum=0
	mul=0
	if "" not in [a, b]:
		a, b=int(a), int(b)
		sum=a+b
		mul=a*b
	response_body=html % {
	"sum":sum,
	"mul":mul,
	}

	start_response("200 OK", [
		("Content-Type", "text/html"),
		("Content-Length", str(len(response_body)))
	])
	return [response_body]
