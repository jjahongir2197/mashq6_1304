from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def fruits():

    fruits = [
        "Apple",
        "Banana",
        "Cherry",
        "Watermelon",
        "Peach",
        "Strawberry"
    ]

    fruit_lengths = []

    for f in fruits:

        fruit_lengths.append({

            "fruit": f,
            "length": len(f)

        })

    longest = max(fruits, key=len)
    shortest = min(fruits, key=len)

    return render_template(
        "index.html",
        fruit_lengths=fruit_lengths,
        longest=longest,
        shortest=shortest
    )


if __name__ == "__main__":
    app.run(debug=True)
