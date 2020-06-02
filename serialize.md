from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

Serialize:
post1 = Post(title='First Post', content='this is first post', author='Aniket')
post1.save()
serializer1 = PostSerializer(post1)
serializer1.data
content1 = JSONRenderer().render(serializer1.data)
content1

De-Serialize:
import io
stream1 = io.BytesIO(content1)
data1 = JSONParser().parse(stream1)
serializer1 = PostSerializer(data=data1)
serializer1.is_valid()
serializer1.validated_data
serializer1.save()

Make POST request:
http POST http://localhost:8000/ title="From console" content="From Console" author="andya"

Make POST request with auth:
http -a <<username>>:<<password>> POST http://localhost:8000/ title="From console" content="From Console" author="andya"
e.g.
http -a admin:1234 POST http://localhost:8000/ title="From console" content="From Console" author="andya"
