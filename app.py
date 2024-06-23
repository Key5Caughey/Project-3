# Importing all the good stuff
from flask import Flask, jsonify, render_template_string, render_template
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Setting up my Flask app
app = Flask(__name__)

# Let's get that database connected
engine = create_engine('sqlite:///social_media_data.db')

# Time to load up the data when the app starts
df1 = pd.read_sql_query("SELECT * FROM us_social_media", engine)
df2 = pd.read_sql_query("SELECT * FROM google_trends", engine)

@app.route("/")
def home_page():
    return("<h1>This is the Landing page</h1>")

# Here's my route for the US social media data
@app.route("/api/v1.0/us_social_media")
def us_social_media():
    # Converting the DataFrame to a dictionary
    data = df1.to_dict(orient='records')
    # Sending it off as JSON
    return jsonify(data)

# And here's my route for the Google trends data
@app.route("/api/v1.0/google_trends")
def google_trends():
    # Again, converting the DataFrame to a dictionary
    data = df2.to_dict(orient='records')
    # Off it goes as JSON
    return jsonify(data)

# Now, let's make a pretty plot
@app.route("/plot")
def plot():
    # Creating a line plot with Plotly Express
    fig = px.line(df1, x='Date', y='Facebook')
    
    # Converting the plot to HTML
    plot_html = pio.to_html(fig, full_html=False)
    
    # Sending the plot as HTML
    return render_template("plot.html", plot=plot_html)

# Time to run the app!
if __name__ == '__main__':
    app.run(port=3000, debug=True)