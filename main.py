from views import *
from model import *

dev_analysis = Developer(analyze_languages(), analyze_contributions(), analyze_years_active())
print(dev_analysis.__dict__)