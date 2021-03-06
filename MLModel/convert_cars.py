from sklearn.linear_model import LinearRegression
import pandas
import coremltools

data = pandas.read_csv("cars.csv")

model = LinearRegression()
model.fit(data[["model", "premium", "battery", "mileage", "condition"]], data["price"])

coreml_model = coremltools.converters.sklearn.convert(model, ["model", "premium", "battery", "mileage", "condition"], "price")
coreml_model.author = "Mohammed Al-Dahleh"
coreml_model.license = "CC0"
coreml_model.short_description = "Predicts the trade-in price of a Tesla car."

coreml_model.save("Cars.mlmodel")