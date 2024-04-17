
<a name="readme-top"></a>
Building an API integrating a ML model using FastAPI.
<div align="center">
  <h1><b>Sepsis_Prediction_API</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents
- [📗 Table of Contents](#-table-of-contents)

- [Sepsis_Prediction_API]

  - [🛠 Built With ](#-built-with-Python)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 live Link ](#-live-link-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)
  

<!-- PROJECT DESCRIPTION -->

# Sepsis_Prediction_API <a name="about-project"></a>

**Sepsis_Prediction_API** Building a Sepsis Prediction API with FastAPI
The primary objective is to leverage this dataset to develop a predictive model that can effectively identify individuals at risk of developing sepsis during their ICU stay. By doing so, healthcare professionals can receive early warnings, allowing them to initiate timely interventions and potentially save lives.

Features

1. **Plasma_glucose**: plasma glucose of the patient
2. **Blood_Work_R1**: blood group of the patient
3. **Blood_Pressure**: blood pressure of the patient
4. **Blood_Work_R2**: blood work R2 of the patient
5. **Blood_Work_R3**: blood work R3 of the patient
6. **BMI**: bmi of the patient
7. **Blood_Work_R4**: blood work R4 of the patient




## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">FastAPI</a></li>
  </ul>
</details>

<details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">ML</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **A data application that presents visualizations on both the exploratory data and the KPIs**
- **A predicitons page to predict by specifying the model you want to use**
- **View proprietory data loaded in real-time form the remote server**
- **Predictions are save for further analysis in the future and users can view the history of their prediction input values**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

![image]

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- FastAPI

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/CodeGraceWanjiku/Sepsis_Prediction_API.git
```

Change into the cloned repository

```sh
  cd Sepsis_Prediction_API
  
```

Create a virtual environment

```sh

python -m venv virt_env

```

Activate the virtual environment

```sh
    virt_env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
    uvicorn main:app --reload

```

- A webpage opens up to view the API
- Navigate to http://127.0.0.1:8000/docs to view the predictions

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Grace Wanjiku-Wanjiru**

- GitHub: [GitHub Profile](https://github.com/CodeGraceWanjiku)
- Twitter: [Twitter Handle](https://twitter.com/shixay)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/grace-w-wanjiru/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PAGE SCREENSHOTS-->

## 🔭 Page Screenshots <a name="Page-Screenshots"></a>

- **FastAPI**
![image](https://raw.githubusercontent.com/CodeGraceWanjiku/SEPSIS_PREDICTION_API/main/assets/Screenshot%202024-04-17%20at%2021.50.39.png)

  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Live URL <a name="support"></a>

This is the link to the API

<p align="left">(<a href="http://127.0.0.1:8000">Live link</a>)</p>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


