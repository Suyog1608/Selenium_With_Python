# Selenium_With_Python
<h4>Test Automation using with Python-Selenium</h4>
<p>Good to have basic knowledge of python and html</p>

<h5>Why do we need to automate tests</h5>
<ol>
  <li>Decreased cost and time of testing</li>
  <li>Enable continuous delivery through round-the-clock testing</li>
  <li>Ensure regression testing</li>
  <li>Increased test coverage</li>
  <li>Cross-device testing made easy</li>
</ol>

<p><b>Mike cohn's test automation pyramid</b></p>
<ul>
    <b>[ User Interface tests <-- Service/API layer tests <-- Unit test ]</b><br><br>

  <li>Unit tests which is the bottom most layer of pyramid which is most numerous and have maximum coverage, <br>
  Used to test small line of code and hence can not be used for integration testing or system testing.</li>
  <li>Service/APi layer tests functionality in terms of services, <br>
  Service means an program where application takes input to produce the outputs,<br>
  Main aim is to seperate UI testing from functionality testing, therby saving the cost and time of UI testing</li>
  <li>UI layer is used to test only the functionality of UI elements</li>
</ul>
<p>
  <b>Python in Automated testing</b>
  <ul>
    <li>provides diff tools for Unit testing and API testing like : unittest, pytest, nose</li>
    <li>for UI level of testing mostly tools are used Selenium and Python</li>
  </ul>
</p>

<p>
  <b>Selenium Autmation Framework</b>
  <li> Selenium Automate browsers </li>
  <li> Used for web UI automation -- the automatic execution of the actions performed in a web browser window</li>
  <li> Used for robust, browser-based regression testing</li>
  <li> Used to scale tests to multiple browsers and environment using Selenium</li>
  <li> Selenium webdriver supports various browsers including Firefox, Chrome, Internet Explorer, Edge, and Safari</li>
  <li> Ensure Cross-crowser compatibility</li>
</p>

<p> <b>Selenium-Firefox Driver</b>
  <li>Firefox binary needs to be installed seperately</li>
  <li>Firefox Driver should be placed in the systems path such that webDriver can locate it automatically</li>
  <li>An Instance of firefox Driver is Created
    <ul> driver = webdriver.Firefox() </ul>
  </li>
  <li> For more info visit this website 
    <ul> https://www.selenium.dev/documentation/webdriver/browsers/firefox/ </ul>
  </li>
</p>

<p> <b>Selenium-Chrome Driver</b>
  <li>Chrome binary needs to installed seperately</li>
  <li>Chrome Driver should be placed in the systems path such that webDriver can locate it automatically</li>
  <li>An Instance of chrome Driver is Created
    <ul> driver = webdriver.Chrome() </ul>
  </li>
  <li> For more info visit this website 
    <ul> https://www.selenium.dev/documentation/webdriver/browsers/chrome/ </ul>
  </li>
</p>

<h4> <b>Note : Before getting started with writing test cases all the installed webdrivers should be placed in Systems path so for getting locate automatically by webdriver</b></h4>


<h4>HTML DOM STRUCTURTE</h4>
<ol>
  <li>The html DOM defines the logical structure of documents and the way a document is accessed and manipulated.</li>
  <li>The DOM presents an HTML Document as a tree structure (a node tree), with elements, attributes, and text</li>
  <li>With the DOM, programmers can create and build documents, navigate their structure, and add, modify, or delete elements and content</li>
</ol>

<p> Let's start with locating the elements by ID
<ul>
  <li>The HTML id attribute specifies a unique id for a HTML element</li>
  <li>Rules for the id attribute
  <ul>
    <li> At lease one character </li>
    <li> No spaces characters </li>
    <li> Case Sensitive </li>
    <li> Unique in the document </li>
  </ul>
  </li>
</ul>
</p>

<b>Let's start with practical now with locating the elements with the different ways</b>
<ul>
  <li>Locating elements by ID</li>
  <li>Locating elements by Name</li>
  <li>Locating elements by XPath
  <ul>
    <li>XPath stands for XML path language</li>
    <li>XPath uses path expressions to identify and navigate nodes in an XML Document</li>
    <li>XPath  is used to locate elements when a specific ID or name is not available for the node.<br>
      It can be used to select one or more nodes in the document - using absolute and relative paths.</li>
    <li>In case of Absolute Path, the path of the name is specified right from the root node.</li>
    <li>In case of Relative Path, the path of the node is specified relative to another node that has relative attribute.</li>
    <li><b>Note:</b> It is generally advised to not use and absolute XPath as even the slightest change in application structure could cause it to fail and become invalid.</li>
  </ul>
  </li>
  <li>Locating elements by class</li>
</ul>
