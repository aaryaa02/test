from flask import Flask,render_template,request,jsonify
from src.pipline.predict_pipline import PredictPipline,CustomData
from src.logger import logging


application = Flask(__name__)
app = application


@app.route("/",methods = ["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")

    else:
        data = CustomData(
            SEX = int(request.form.get("SEX")),
            EDUCATION = int(request.form.get("EDUCATION")),
            AGE = int(request.form.get("AGE")),
            PAY_0 = int(request.form.get("PAY_0")),
            PAY_2 = int(request.form.get("PAY_2")),
            PAY_3 = int(request.form.get("PAY_3")),
            PAY_4 = int(request.form.get("PAY_4")),
            PAY_5 = int(request.form.get("PAY_5")),
            PAY_6 = int(request.form.get("PAY_6"))
            )
        

        final_data = data.get_data_as_data_frame()
        predict_pipline = PredictPipline()
        pred = predict_pipline.predict(final_data)

        result = pred

        if result == 1:
            return render_template("form.html",final_result = "The Credit Card Holder Will Be Defaulter in Next Month:{}".format(result))
        elif result == 0:
            return render_template("form.html",final_result = "The Credit Card Holder Will Not Be Defaulter in Next Month:{}".format(result))


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
