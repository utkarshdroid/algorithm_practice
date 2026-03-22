import math

class MyStandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, data):
        # 1. Calculate Mean
        # 2. Calculate Standard Deviation
        # 3. Store them in self
        if data and len(data)>0:
            data = [i for i in data if i is not None]
            self.mean = sum(data)/len(data)
        variance = [math.pow((self.mean-i),2) for i in data]
        self.std = math.pow(sum(variance),0.5)/len(data)


    def transform(self, data):
        scaled_data = []
        for x in data:
            if x is None:
                scaled_data.append(None) # Keep Nones as Nones
                continue
            if self.std == 0:
                    # If no variation, the value is essentially 0 distance from mean
                    scaled_data.append(0.0)
            z_score = (x - self.mean) / self.std
            scaled_data.append(z_score)
        return scaled_data
    


# --- Test Data ---
train_points = [10, 20, 30, 40, 50]
test_points = [15, 25]

scaler = MyStandardScaler()
scaler.fit(train_points)
print(f"Scaled Test Data: {scaler.transform(test_points)}")