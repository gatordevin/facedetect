import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
from threading import Lock
# import rospkg
import os

class ImagePipeline(Node):
    def __init__(self):
        super().__init__('my_node')
        self.mutex = Lock()
        self.bridge = CvBridge()
        topic = '/camera/color/image_raw'
        self.subscription = self.create_subscription(Image, topic, self.image_callback, 10)
        self.publisher = self.create_publisher(Image, '/out/image', 10)
        # print current path
        path = os.path.dirname(os.path.realpath(__file__))
        print(f"Package path: {path}")

    def image_callback(self, inp_im):
        try:
            imCV = self.bridge.imgmsg_to_cv2(inp_im, "bgr8")
        except CvBridgeError as e:
            self.get_logger().info('CvBridgeError: {}'.format(e))
            return

        if imCV is None:
            self.get_logger().info('Frame dropped, skipping processing')
        else:
            self.image_processor(imCV)

    def image_processor(self, imCV):
        self.get_logger().info("Processing image")
        # Face detect
        face_cascade = cv2.CascadeClassifier('/data/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(imCV, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        print(f"Found {len(faces)} faces")
        for (x, y, w, h) in faces:
            cv2.rectangle(imCV, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Publish
        try:
            out_msg = self.bridge.cv2_to_imgmsg(imCV, "bgr8")
            self.publisher.publish(out_msg)
        except CvBridgeError as e:
            self.get_logger().info('CvBridgeError: {}'.format(e))

def main(args=None):
    rclpy.init(args=args)
    pipeline = ImagePipeline()
    rclpy.spin(pipeline)
    pipeline.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
