<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

    <title>Signup</title>
</head>
<body>
<style>
    body {
        margin-top: 50px;
    }
    label {
        float: left;
    }
    .block {
        text-align: right;
    }
    .btn-sign-up {
        margin: 10px 0 0 0;
    }
    .title {
        text-align: center;
        margin-bottom: 15px;
    }
</style>
    <div class="title"><h1>Registration</h1></div>
    <div class="block col-md-6">
        <form action="signup.php" method="post" class="form-inline">
            <div class="form-group">
                <label for="exampleInputEmail">Email</label><br />
                <input type="email" name="email" class="form-control" id="inputEmail" placeholder="Email address">
            </div><br />
            <div class="form-group">
                <label for="exampleInputPassword">Password</label><br />
                <input type="password" name="password" class="form-control" id="inputPassword" placeholder="Password">
            </div><br />
            <div class="form-group">
                <button type="submit" class="btn btn-primary btn-sign-up">Sign in</button>
            </div>
        </form>
    </div>
<div class="col-md-6">
    <h4>If you have an account press</h4>
    <div class="content-link"><a href="login.php" class="btn btn-default">Authorize</a></div>
</div>
</body>
</html>