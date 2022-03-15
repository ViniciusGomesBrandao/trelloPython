import trello
client = trello.client('14b1070ecb225a3e0eb448f40c0f2ad9', 'a6f0ecacfc74673735a9091bb212f67edc5d66c06bc6f8b760b40ef12dd2d0d2')
data = client.get("/boards/622f5e933b6a1e11b6885461")
print({data['name']})