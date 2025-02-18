from pathlib import Path
from swbf.formats.sky import SKY

file = Path('C:/Users/Chris/Kruschd/SWBFDocumentation/jed1.sky')
SKY.read(filepath=file)