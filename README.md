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
  <li>Locating elements by class
  <ul>
    <li>The HTML class attribute specifies one or more class names for an HTML element</li>
    <li>These class names are used to point a class in a stylesheet</li>
    <li>It is Used to locate elements when the class attribute of one or more elements is known</li> 
  </ul>
  </li>
</ul>

# Let's get ahead with some new methods for testing
<p><b>PAGE INTERACION</b></p>
<ul>
  <li>Just landing on a page and locating elements is not enough</li>
  <li>Interact with the elements on the page once they are selected</li>
  <li>Interact with a page as actions performed by a user.</li>
  <li>In this we will learn about how to put values in text inputs and text areas (like search boxes, etc.) and can test the results by importing the <b>'Keys' Module</b></li>
</ul>

<p><b>Filling Forms</b></p>
<ul>
  <li>Dealing with other form of elements</li>
  <li>"Select" class that helps us tackle select elements - find a select element and then select values by index, visible text, and value</li>
  <li>"Submit" method on every element in the form</li>
  <li>In this we will use the <b>SELECT class</b> which helps you deal with select elements in the form & it also comes with a submit method that works on every element in the form</li>
</ul>

<p><b>Drag and Drop</b></p>
<ul>
  <li>Users drag and drop elements as part of a UI interaction</li>
  <li>Drag and drop source element to a target element</li>
  <li>Drag and drop a source element by a specific x-offset and y-offset</li>
  <li>This can be implement by using <b>ActionChains Class</b> which will help in perfforming drag n drop and also setting in the values of <b>xoffset and yoffset</b> which can be perform by <b>perform() function</b></li>
</ul>

<h2>Let's go ahead with getting understand of what are Waits and why  do we need them</h2>
<ul><b>What are Waits?</b>
  <li>Waits are very important when it comes to placing your automation script.</li>
  <li> Because most websites used Asynchronous Techniques such as AJAX.
    <ul>
    <li>When a webpage is loaded by the browser the elements may be loaded at different time intervals due to AJAX calls.</li>
    <li>Some elements may take much longer to load as compared to others. This could be something like a image, video or any other element that requires more time to load.</li>
    <li>Which posses a problem while locating elements on a page</li>
    <li>If an element is not found by a script at that time, an exception is raised and your script will run into a issue and stop
    </ul>
  </li>
  <li>Waiting adds a time interval between actions performed by the Web driver <br> i.e it adds a time wait between locating elements and performing operations on them.</li>
</ul>

<b>Selenium Webdriver provides two types of wait i.e Explicit Waits and Implicit Waits</b>
<ul>
<li>An explicit waits stops execution until a certain condition is satisfied., and</li>
<li>An implicit waits Polls the DOM for a given amount of time while trying to locate an element.</li>  
</ul>

<h4>Explicit Wait</h4>
<ul>
  <li>Explicit wait is one where you want your code to pause until a certain condition has been satisfied.</li>
  <li>Like if you are testing an image and you want to wait for the presence of the image to be loaded, then you add explicit wait,<br>
  otherwise the image will not load at right time in your script and element not found exception will be thrown.</li>
  <li>Selenium webdriver uses a combination of the classes WebDriverWait and ExpectedConditions to add explicit waits.</li>
  <li>These convinient methods could test conditions ranging from the title list to visibility of an element being located to an alert being present, to text being present, and much more.</li>
</ul>

<h4>Implicit Wait</h4>
<ul>
  <li>An implicit wait is where you want your code to pause for a certain amount of time beofre every action or every element to be loaded.</li>
  <li>Pauses for a certain amount of time for every action.</li>
  <li>Waiting time is specified in seconds.</li>
  <br>
  Use Case
  <li>The typical use case for implicit waits is when you have a slow internet connection and you know that every element im the site will load much slowly than expected</li>
  <li>So we can add implicit wait before every call, so once the element is loaded, If the element is loaded in the specified time then the script moves on <br>
  If the element is not loaded within the specified amount of time, then an exception is thrown.</li>
</ul>
