<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Animated Visme-like Form</title>
  <style>
    :root {
      --blue1:#4b6cff;
      --blue2:#5f95f5;
      --accent:#22c55e;
      --accent-hover:#16a34a;
    }
    * { box-sizing:border-box; }
    body {
      margin:0;
      height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      font-family:"Segoe UI", sans-serif;
      overflow:hidden;
      color:#333;
      background:linear-gradient(-45deg, var(--blue1), var(--blue2), #3b82f6, #1d4ed8);
      background-size:400% 400%;
      animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
      0% {background-position:0% 50%}
      50%{background-position:100% 50%}
      100%{background-position:0% 50%}
    }

    .container {
      display:flex;
      align-items:center;
      gap:3rem;
      animation: fadeIn 1.2s ease-in-out;
    }
    @keyframes fadeIn {
      from {opacity:0; transform:translateY(40px);}
      to {opacity:1; transform:translateY(0);}
    }

    .character img {
      max-width:380px;
      animation: float 5s ease-in-out infinite, fadeInLeft 1.2s ease;
    }
    @keyframes float {
      0%,100%{transform:translateY(0)}
      50%{transform:translateY(-15px)}
    }
    @keyframes fadeInLeft {
      from {opacity:0; transform:translateX(-80px)}
      to   {opacity:1; transform:translateX(0)}
    }

    .form-box {
      width:380px;
      background:#fff;
      padding:2rem;
      border-radius:20px;
      box-shadow:0 20px 50px rgba(0,0,0,0.25);
      position:relative;
      overflow:hidden;
    }

    .step {
      position:absolute;
      top:0; left:0; right:0; bottom:0;
      padding:2rem;
      opacity:0; 
      pointer-events:none;
      transform:translateX(50px);
      transition:all .6s ease;
    }
    .step.active {
      opacity:1;
      pointer-events:auto;
      transform:translateX(0);
    }
    .step.exit-left {
      opacity:0;
      transform:translateX(-60px);
    }

    h2 {
      margin:0 0 1rem;
      font-size:1.4rem;
      text-align:center;
      animation: fadeInUp .8s ease;
    }
    @keyframes fadeInUp {
      from {opacity:0; transform:translateY(30px);}
      to {opacity:1; transform:translateY(0);}
    }

    .field {
      display:flex;
      align-items:center;
      background:#f8fafc;
      border-radius:12px;
      padding:.9rem 1rem;
      margin:1rem 0;
      transition:all .3s;
    }
    .field:focus-within {
      background:#fff;
      box-shadow:0 6px 20px rgba(0,0,0,0.15);
      transform:scale(1.03);
    }
    .field input {
      border:none;
      outline:none;
      background:transparent;
      width:100%;
      font-size:1rem;
    }

    .btn {
      display:block;
      width:100%;
      padding:1rem;
      margin-top:1rem;
      border:none;
      border-radius:12px;
      font-size:1.2rem;
      font-weight:bold;
      color:#fff;
      background:var(--accent);
      cursor:pointer;
      position:relative;
      overflow:hidden;
      transition:transform .2s ease;
    }
    .btn:hover {
      background:var(--accent-hover);
      transform:translateY(-3px);
      box-shadow:0 10px 25px rgba(0,0,0,0.2);
    }
    .btn:active {transform:scale(0.97);}
    .btn::after {
      content:"";
      position:absolute;
      width:20px;height:20px;
      background:rgba(255,255,255,0.6);
      border-radius:50%;
      transform:scale(0);
      opacity:0;
      pointer-events:none;
      animation:ripple .6s linear;
    }
    @keyframes ripple {
      to {
        transform:scale(15);
        opacity:0;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="character">
      <img src="https://cdn3d.iconscout.com/3d/premium/thumb/businessman-5678594-4731219.png" alt="3D Character">
    </div>

    <div class="form-box">
      <!-- Step 1 -->
      <div class="step active" id="step1">
        <h2>What’s your name?</h2>
        <div class="field"><input type="text" id="fname" placeholder="First Name"></div>
        <div class="field"><input type="text" id="lname" placeholder="Surname"></div>
        <button class="btn" onclick="nextStep(2)">Next</button>
      </div>

      <!-- Step 2 -->
      <div class="step" id="step2">
        <h2>Enter your email address</h2>
        <div class="field"><input type="email" id="email" placeholder="Ex. yourname@company.com"></div>
        <button class="btn" onclick="nextStep(3)">Next</button>
      </div>

      <!-- Step 3 -->
      <div class="step" id="step3">
        <h2>Create a password</h2>
        <div class="field"><input type="password" id="pass" placeholder="Password"></div>
        <button class="btn" onclick="nextStep(4)">Register</button>
      </div>

      <!-- Step 4 -->
      <div class="step" id="step4">
        <h2>🎉 Welcome aboard!</h2>
        <p style="text-align:center; font-size:1.1rem;">Your account has been created.</p>
      </div>
    </div>
  </div>

  <script>
    let current = 1;
    function nextStep(n){
      const currStep = document.getElementById(`step${current}`);
      const next = document.getElementById(`step${n}`);
      if(currStep){
        currStep.classList.remove('active');
        currStep.classList.add('exit-left');
      }
      if(next){
        next.classList.add('active');
      }
      current = n;
    }

    // ripple effect
    document.querySelectorAll('.btn').forEach(btn=>{
      btn.addEventListener('click', function(e){
        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;
        let ripple = document.createElement("span");
        ripple.style.left = x + "px";
        ripple.style.top = y + "px";
        ripple.classList.add("ripple");
        this.appendChild(ripple);
        setTimeout(()=>ripple.remove(), 600);
      });
    });
  </script>
</body>
</html>
