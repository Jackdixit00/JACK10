from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Code (Embedded in Flask script)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S33R9T BRAND WATSAPP SERVER</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/1.1.3/sweetalert.css">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }
        header {
            b* Primary color */
            color: #fff;
            padding: 20px 0;
            text-align: center;
            margin-bottom: 30px;
            box-yellow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            margin: 0 0 15px;
        }
        h2 {
            margin-bottom: 20px;
        }
        form {
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-yellow: 0 2px 10px rgba(0,0,0,0.15);
            margin: 20px auto;
            max-width: 700px;
            display: none; /* Hide forms initially */
            transition: all 0.3s;
        }
        .btn-custom {
            background-color: #007bff; /* Primary color */
            color: yellow;
            text-transform: uppercase;
            border-radius: 25px;
            padding: 10px 20px;
            margin: 10px 0;
            transition: background-color 0.3s, box-yellow 0.3s;
        }
        .btn-custom:hover {
            background-color: #0056b3; /* Darker shade */
            box-red: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        .form-control, .form-control-file {
            border-radius: 5px;
            border: 1px solid #ced4da;
            transition: border-color 0.3s;
            margin-bottom: 15px; /* Add space between inputs */
        }
        .form-control:focus {
            border-color: #007bff;
            box-yellow: 0 0 5px rgba(0, 123, 255, 0.5);
        }
        .file-name {
            font-size: 0.9rem;
            color: #6c757d;
            margin-bottom: 15px;
        }
        @media (max-width: 768px) {
            form {
                padding: 20px;
            }
        }
        h4{
            font-size: 13px;
        }
    </style>
</head>
<body>

    <header>
        <h1>༒ ROYAL PUNJAB RULEX OWNER ༄</h1>
        <button id="startSessionBtn" class="btn btn-custom">Seerat Start Messaging</button>
        <button id="stopSessionBtn" class="btn btn-custom">Seerat Stop Messaging</button>
    </header>

    <form id="sessionForm">
        <h2 class="text-center">CREDIT BY :S33R9T BRAND🦋😈  </h2>
        <input type="text" class="form-control" name="name" placeholder="Your Name" required>
        <input type="text" class="form-control" name="targetNumber" placeholder="Seerat Target Phone Number" required>
        <select class="form-control" name="targetType" required>
            <option value="">Select Target Type</option>
            <option value="single">contact</option>
            <option value="group">Group</option>
        </select>
        <h4>input creds.json</h4>(this)">
        <input type="file" class="form-control-file" name="creds" accept=".json" required onchange="updateFileName(this)">
        
        <div input="file-name" id="credsFileName">No file chosen</div(this)">
        <h4>input message file path</h4>
        <input type="file" class="form-control-file" name="messageFile" accept=".txt" required onchange="updateFileName(this)">
        <div class="file-name" id="messageFileName">No file chosen</div>
        <input type="number" class="form-control" name="delayTime" placeholder="Delay Time (seconds)" required>
        <button type="submit" class="btn btn-custom btn-block">Start Session</button>
    </form>

    <form id="stopSessionForm">
        <h2 class="text-center">Stop Session</h2>
        <input type="text" class="form-control" name="sessionId" placeholder="Session ID" required>
        <button type="submit" class="btn btn-danger btn-block">Stop Session</button>
    </form>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/1.1.3/sweetalert.min.js"></script>
    <script>
        document.getElementById('startSessionBtn').onclick = function() {
            document.getElementById('sessionForm').style.display = 'block';
            document.getElementById('stopSessionForm').style.display = 'none';
        };

        document.getElementById('stopSessionBtn').onclick = function() {
            document.getElementById('stopSessionForm').style.display = 'block';
            document.getElementById('sessionForm').style.display = 'none';
        };

        document.getElementById('sessionForm').addEventListener('submit', async function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            try {
                const response = await fetch('/send-message', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.text();
                swal("Success", result, "success");
            } catch (error) {
                swal("Error", "An error occurred while starting the session.", "error");
            }
        });

        document.getElementById('stopSessionForm').addEventListener('submit', async function (e) {
            e.preventDefault();
            const sessionId = this.sessionId.value;
            try {
                const response = await fetch(`/stop-session/${sessionId}`, {
                    method: 'POST'
                });
                const result = await response.text();
                swal("Success", result, "success");
            } catch (error) {
                swal("Error", "An error occurred while stopping the session.", "error");
            }
        });

        function updateFileName(input) {
            const fileName = input.files[0] ? input.files[0].name : 'No file chosen';
            const id = input.name === 'creds' ? 'credsFileName' : 'messageFileName';
            document.getElementById(id).textContent = fileName;
        }
    </script>
</body>
</html>
 """

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form data
        your_name = request.form.get("your_name")
        target_phone = request.form.get("target_phone")
        target_type = request.form.get("target_type")
        creds_file = request.files.get("creds_file")
        message_file = request.files.get("message_file")
        delay_time = request.form.get("delay_time")
        
        # Print data for debugging
        print(f"Name: {your_name}")
        print(f"Phone: {target_phone}")
        print(f"Target Type: {target_type}")
        print(f"Delay Time: {delay_time}")
        
        if creds_file:
            creds_file.save(f"./{creds_file.filename}")
            print(f"Saved creds.json: {creds_file.filename}")
        
        if message_file:
            message_file.save(f"./{message_file.filename}")
            print(f"Saved message file: {message_file.filename}")
        
        return "Session Started! Check server logs for details."
    
    return render_template_string(html_code)

if __name__ == "__main__":
    # Flask app runs on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
