<h1>MAT492_Fractals Repo</h1>

<h3>MAT 492</h3>
<h3>Term: Spring 2020</h3>

<p>Files used for "Cantor Lawn" research.</p>

<h4>Instructions for installing git, the characters [] should always be ommited:</h4>
<div>
  <ol>
    <li><a href="https://git-scm.com/downloads" target="_blank">Download Git</a></li>
    <li>Click on "Clone or Download" above and copy the URL to your clipboard.</li>
    <li>Open terminal of choice: <br/>
      [Win Key] and type "cmd" to open command prompt</li>
    <li>Type the command:<br/>
      git clone [url] [directory]<br/>
      Note: directory is your choice! If directory is ommited Git will create a new directory with the name of the repo.</li>
    <li>You're all set! Go to <a href="https://git-scm.com/" target="_blank">Git</a> for lists of commands and specifics..</li>
  </ol>
  <br/>
  <p>
    If you prefer to use a GUI to interact with Git, <a href="https://www.sourcetreeapp.com/" target="_blank">Source Tree</a>
    is a really nice tool to avoid using a terminal.  <a href="https://www.gitkraken.com/" target="_blank">Git Kraken</a>
    is personally my favorite GUI for Git, I use it at my internship, but you can only view private repositories with the paid
    version in GitKraken.
  </p>
</div>

<h4>Python:</h4>
<div>
  <p>To run the python files, <a href="https://www.python.org/downloads/" target="_blank">Python</a> must be installed.
     The link will navigate you where to install python, the most recent version is 3.8.1. When running the installer, 
     BE SURE to CHECK any checkbox that has anything to do with setting path variables, otherwise it will have to be done 
     manually at somepoint.
  </p>
  <p>
     You can verify everything installed properly by entering the following commands in the terminal from any directory:
  </p>
  <ul>
    <li>python --version</li>
    <li>pip --version</li>
  </ul>
  <p>
     After the installation is complete, you will need to use PIP to install the necessary libraries. This is where its important to
     have the path variable set, installing python above version 2.7.9 installs pip automatically and sets the path variable. The
     following commands install the necessary libraries from any terminal:
  </p>
  <ul>
    <li>pip install matplotlib</li>
    <li>pip install Pillow</li>
    <li>pip install enum34</li>
  </ul>
</div>
<h4>Links to Python Libraries</h4>
  <ul>
    <li><a href="https://matplotlib.org/" target="_blank">MatPlotLib</a></li>
    <li><a href="https://pillow.readthedocs.io/en/stable/" target="_blank">Pillow</a></li>
  </ul>
