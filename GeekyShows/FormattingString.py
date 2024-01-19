# Format() Method
from datetime import datetime
today = datetime(2019, 10, 5)
print(f"{today}")
print(f"{today: %d-%b-%y}")