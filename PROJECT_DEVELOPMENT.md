# **11SE Task 1 2025**

### **By Shawn Fan**

# **Requirements Definition**

## **Functional Requirements**
- **Data Retrieval:** What does the user need to be able to view in the system?

The user needs to be able to access and view all of the data from the API, and be able to view the configured dataset. The user should also be able to view errors due to missing data, it should be able to specify whether there is data or not. For example, for an NBA stats database, if the dataset did not include the date-of-birth, then it should say something like N/A, not displaying an error since the information is only unavailable.

- **User Interface:** What is required for the user to interact with the system?

For the user to interact with the system, there must be at least a command-line interface for the UI, which will allow the user to understand what is happening, and be able to use the application without any bugs or problems. The user should be able to use the UI to connect and interact with the API. The UI should also have the correct formatting, be readable and understandable, and be clear and concise to interact with. The program should also be able to configure the dataset for some sections of the dataset, for example, showing the descending order for a chosen row/column.

- **Data Display:** What information does the user need to obtain from the system?

The user needs to be able to obtain selected data from the database, the original data from the database, and any error messages or outputs from unavailable data or bugs, as well as the configured/formatted dataset. The user should also be able to obtain a dataset that is configured to their desire, with the rows and columns they want to see to take in the information provided.

## **Non-Functional Requirements**
- **Performance:** How well does the system need to perform? 

The system needs to be quick and efficient so the sorting and displaying of the data isn't slow. This isn't really hard to achieve as python is a pretty fast programming language, and with the help of other modules, the speed and efficiency can be optimised.

- **Reliability:** How reliable does the system and data need to be?

The system and data should be always reliable as it is only the API that affects reliability since it's out of my control. Unreliable or undeveloped APIs could cause problems in the system, so it is important to avoid them for the reliability of a system and dataset. You can find the API used in this project or other reliable APIs off https://github.com/public-apis/public-apis as it provides a list of good APIs for many different topics.

- **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

The system should be concise and efficient, only providing the information that the user specifies. The instructions can be found in the READ.md file contained in this program, providing a guide for how to use it, and how to install the required dependencies.

# **Determining Specifications**
## **Functional Specifications** ##
What does the system actually NEED to do?

- **User Requirements**

The user must be able to view the data from the API.

- **Inputs & Outputs**

It needs to accept the requests from the user and display the request.

- **Core Features**

The program must communicate with the API, retrieve the data and display it.

- **User Interaction**

The program will have a command-line UI and it will provide the commands for the API to get the data and information for the user to view

- **Error Handling**

The most probable error would be one where the location is misspelt, or the data is missing for a city, due to the API not including it. To handle the error, the system should output "Error occurred, make sure to check your spelling and try again, if this error persists, the information on your location is unavailable.".

## **Non-Functional Specifications** ##
What would improve the system but is ultimately not required?

- **Performance**

How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?

- **Usability / Accessibility**

How might you make your application more accessible? What could you do with the User Interface to improve usability?

- **Reliability**

What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Duplicate data? API retrieval crash?

# **Design**

# **Development**

# **Integration**

# **Testing and Debugging**

# **Installation**

# **Maintenance**
``````
