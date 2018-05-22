import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBAGAkKwT7mLDXJ6M0ZBCqGfM6ANM3XulZCAujC3vS12CReDIDthOtR3O5YQVODrhTZCtzw3I4nTHCNj9e6nQb2ZAWsaq9xJprBpLjiXxNKzZAdcgWz7dZANj4gv8SipDyFaxL8WaiLfGP2NSWPFIO6qn4cAygefgCXx5reeFuZBnwLbissZBLzpJ0O1erJ2LpCAZDZD"

# Message to post as status on Facebook
status = "ab"

# Authenticating
graph = fb.GraphAPI(access_token)

post_id = graph.put_wall_post(status)

image=open('sample.jpg', 'rb')
graph.put_photo(image.read(),
                message='Look at this cool photo!')
