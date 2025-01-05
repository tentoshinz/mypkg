import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("listener")


# def cb(msg):
#     global node
#     node.get_logger().info("Listen: %s" % msg) 


def main():
    client= node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('taikityuu')

    req= Query.Request()
    req.name= "kami"
    future= client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response= future.result()
            except:
                node.get_logger().info('yobidasi sippai')
            else:
                node.get_logger().info("age: {}".format(response.age))
            
            break
    node.destroy_node()
    rclpy.shutdown()
    