import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.shipping.transport import Transport

"""create transport entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param method: shipping method you would like
    :type method: str
    :returns: Transport
    :rtype: Transport
"""
def create_transport(method: str) -> Transport:
    try:
        if not isinstance(method, str):
            raise TypeError()

        if method == "ship":
            return Transport.SHIP
        elif method == "train":
            return Transport.TRAIN
        elif method == "truck":
            return Transport.TRUCK
        elif method == "plane":
            return Transport.PLANE
        else:
            # Set truck as default value
            return Transport.TRUCK
    except TypeError:
        return Transport.TRUCK