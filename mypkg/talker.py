import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node= Node('talker')

# pub= node.create_publisher(Person, "person", 10)
# n= 0

# def cd():
#         global n
#         msg= Person()
#         msg.name = "どうも~"
#         msg.age = n
#         pub.publish(msg)
#         n+=1

def cd(request, response):
        if request.name== "kami":
               response.age= 99999
        else:
               response.age= 1
        
        return response


def main():
    srv= node.create_service(Query, "query", cd)
#     node.create_timer(0.5, cd)
    rclpy.spin(node)

