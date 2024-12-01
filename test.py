import sys
# 更換
package_path = r".\python-3.9.12\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


print(np.__version__)