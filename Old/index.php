<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/Chart.min.js"></script>
</head>
<body>

<div class="container">
<h1>LIST FORM!</h1>
  <form class="form-inline m-2" action="create.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" class="form-control m-2" id="name" name="name">
    <label for="age">Age:</label>
    <input type="number" class="form-control m-2" id="age" name="age">
    <button type="submit" class="btn btn-primary">Add</button>
  </form>
  <table class="table">
    <tbody>
      <?php include 'read.php'; ?>
    </tbody>
  </table>
</div>

<div id="graphCanvas"></div>

<script>
        $(document).ready(function () {
            showGraph();
        });


        function showGraph()
        {
            {
                $.post("graph.php",
                function (data)
                {
                    console.log(data);
                    var name = [];
                    var marks = [];

                    for (var i in data) {
                        name.push(data[i].name);
                        marks.push(data[i].age);
                    }

                    var chartdata = {
                        labels: name,
                        datasets: [
                            {
                                label: 'Ages',
                                backgroundColor: '#49e2ff',
                                borderColor: '#46d5f1',
                                hoverBackgroundColor: '#CCCCCC',
                                hoverBorderColor: '#666666',
                                data: age
                            }
                        ]
                    };

                    var graphTarget = $("#graphCanvas");

                    var barGraph = new Chart(graphTarget, {
                        type: 'bar',
                        data: chartdata
                    });
                });
            }
        }
        </script>

</body>
</html>
