import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Please contact https://t.me/gemsoftroy for further information

