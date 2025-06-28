# ENERGY FLOW X (EFX) - HVAC Engineer's Analysis Toolkit

Introducing <strong> Energy Flow X</strong>, an advanced web application for engineers!

| PROJECT LOGO (Copyright pending)                                       | URL's:                                                                                                           |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [![logo-sns.png](assets/images/logo-efx.png)](https://energyflowx.com) | ⇒ [Go to EFX Website](https://energyflowx.com) ⇐ <br><br> ⇒ [Go to EFX Demo API](https://demo.energyflowx.com) ⇐ |

EnergyFlowX integrates the following of my HVAC engineering libraries:
- [HVAC | Engine](https://github.com/pjazdzyk/hvac-engine) - The physics of air with water vapor content including thermodynamic processes,
- [UNITILITY - Spring](https://github.com/pjazdzyk/unitility) - The physical quantity and units of measure conversion handling library,
- [Brent Dekker Solver](https://github.com/pjazdzyk/brent-dekker-solver) - The enhanced implementation of a famous Brent-Dekker numerical scheme for solving nested equations.

This service is dedicated to HVAC/MEP, mechanical engineers, and chemical and process engineers providing accurate calculations of air properties with humidity
content (Psychrometrics) and thermodynamic processes within the typical parameters scope for HVAC industry applications.<br>

#### EnergyFlowX is planned to be commercialized in the coming months, once the testing phase with end users is successfully completed.

> This is not "_just another psychrometrics calculator_." <br>
> It is a **comprehensive engineering software ecosystem**, designed to support the development of complex engineering projects like this one. <br>
> This product is the result of **years of development, with over 10,000 hours** of personal time invested. <br>
> The frontend is merely the crowning jewel — the cherry on top. <br>

To readers unfamiliar with fluid mechanics and thermodynamics, the calculation forms may appear deceptively simple. 
But **trust me** — there’s nothing simple here once you look behind the curtain… <br>

Fluid parameters are not assumed as constants (specific heat, or density as an example) as in many other available psychrometrics tools. 
Every temperature-dependent property is calculated based on equations available in standards (e.g., ASHRAE), scientific journals and papers,
or formulas derived by myself. You can review the full list of reference sources at the end of this documentation.

## WEBSITE AND API
Eager to see how the project works and help HVAC engineers? Visit the site below, register to create your own free 
account, and feel free to explore the site! <br>

If you are a developer interested in creating your own application—check the API demo. I can provide you REST API as a service
so you could focus on your application business layer instead of investing ~10 000 of hours for building backbone physics libraries as I did.
API-As-Service is available only in individual pricing mode. Contact me directly for details!

| CREATED BY (All rights reserved):           | DEVELOPER:                                                                                                                                                         |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![logo-sns.png](assets/images/logo-sns.png) | **Piotr Jazdzyk,** MSc Eng <br> [Read more about the author](https://energyflowx.com/social) <br> [Reach me out on LinkedIn](https://www.linkedin.com/in/pjazdzyk) |

Do not forget to say hello!

Cooling process calculation showcase:
[![logo-sns.png](assets/images/animated/cooling.gif)](https://energyflowx.com/hvac-processes/cooling)

Multiple air stream mixing process showcase:
[![logo-sns.png](assets/images/animated/mixing.gif)](https://energyflowx.com/hvac-processes/mixing)

Humid air thermophysical properties calculation showcase:
[![logo-sns.png](assets/images/animated/humid_air.gif)](https://energyflowx.com/fluid-properties/humid-air)

**NO AI ZONE**. <br>
All calculations use fine crafted algorithms based on existing scientific formulas and equations, implemented from scratch all by myself.
I love AI, but this is not a right project for using LLMs.

---
# DOCUMENTATION

1. [Tech & dependencies](#1-tech-and-dependencies) <br>
2. [System design & architecture](#2-system-design) <br>
3. [Current version](#3-current-version) <br>
4. [Functionality](#4-functionality) <br>
5. [REST API](#5-rest-api) <br>
   5.1 [Api versioning](#51-versioning) <br>
   5.2 [Physical quantity master data](#52-physical-quantities-master-data) <br>
   5.3 [Units of measure conversion](#53-physical-quantities-conversion) <br>
   5.4 [Properties of dry / humid air](#54-physical-properties-of-humid-air) <br>
   5.5 [Heating process](#55-process-of-heating) <br>
   5.6 [Cooling process](#56-process-of-real-cooling-with-condensate-discharge) <br>
   5.7 [Mixing process](#57-process-of-mixing) <br>
   5.8 [Multiple processes in sequence](#58-sequential-process-computation) <br>
   5.9 [Unit Overrides](#59-unit-overrides) <br>
   5.10 [Hydraulic Conduit](#510-hydraulic-conduit) <br>
   5.11 [Error response](#511-error-response) <br>
   5.12 [SwaggerUI](#512-swagger-ui) <br>
6. [Attribution and citation](#6-licensing-attribution-and-citation) <br>
7. [Feature request and bug reporting](#7-feature-request-and-bug-reporting) <br>
8. [Acknowledgments](#8-acknowledgments) <br>
9. [Reference sources](#9-reference-sources) <br>

## 1. TECH AND DEPENDENCIES

<strong>EnergyFlow X</strong> is developed using the following technologies: <br>

Frontend: <br>
![image](https://img.shields.io/badge/Vue%20js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D) &nbsp;
![image](https://img.shields.io/badge/Quasar-1976D2?style=for-the-badge&logo=quasar&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E) &nbsp;
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) &nbsp;
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) &nbsp;

Backend: <br>
![image](https://img.shields.io/badge/21-Java-orange?style=for-the-badge) &nbsp;
![image](https://img.shields.io/badge/apache_maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Junit5-25A162?style=for-the-badge&logo=junit5&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot) &nbsp;
![image](https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=Spring-Security&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) &nbsp;

Infrastructure:<br>
![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Sonar%20cloud-F3702A?style=for-the-badge&logo=sonarcloud&logoColor=white) &nbsp;
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) &nbsp;

Engineering libraries:<br>
[![Unitility](https://img.shields.io/badge/UNITILITY-2.8.0-13ADF3?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMi41bW0iIGhlaWdodD0iMTQuNW1tIiB2aWV3Qm94PSIwIDAgMjI1MCAxNDUwIj4NCiAgPHBvbHlnb24gZmlsbD0iIzUwN0QxNCIgcG9pbnRzPSIyMjQxLjAzLDE1Ljg4IDExMzYuMzgsMTUuODQgOTA1Ljg4LDQxNS4xIDIwMTAuNTMsNDE1LjA5IiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNzFBQjIzIiBwb2ludHM9IjExMTYuMzgsMTUuODQgNjU1Ljk5LDE1Ljg0IDQ5NC4xNSwyOTYuMTcgNzI4LjM1LDY5NC44OCIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzhBQzkzNCIgcG9pbnRzPSI0ODQuMTUsMzA2LjE3IDI1NS4wNiw3MDIuOTYgMzg3LjY2LDkzMi42NCA4NDUuODMsOTMyLjYzIiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNThEMEZGIiBwb2ludHM9Ii03LjE3LDE0NDAuMDkgMTA5Ny45NywxNDQwLjA4IDEzMjguNDcsMTA0MC44MyAyMjMuMzIsMTA0MC44NSIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzEzQURGMyIgcG9pbnRzPSIxNzM5LjA0LDExNjAuOTEgMTUwOS4wOSw3NjIuNjQgMTExNy45NywxNDQwLjA4IDExODYuOTMsMTQ0MC4wOCAxNTc3Ljg3LDE0NDAuMDgiIC8+DQogIDxwb2x5Z29uIGZpbGw9IiMwMzkzRDAiIHBvaW50cz0iMTk3OC44LDc1Mi45NiAxODQ2LjIsNTIzLjMgMTM4Ni42OCw1MjMuMyAxNzQ5LjA0LDExNTAuOTEiIC8+DQo8L3N2Zz4=)](https://github.com/pjazdzyk/Unitility) &nbsp;
[![Brent-Dekker-Solver](https://img.shields.io/badge/Brent_Dekker%20solver-2.10-13ADF3?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMi41bW0iIGhlaWdodD0iMTQuNW1tIiB2aWV3Qm94PSIwIDAgMjI1MCAxNDUwIj4NCiAgPHBvbHlnb24gZmlsbD0iIzUwN0QxNCIgcG9pbnRzPSIyMjQxLjAzLDE1Ljg4IDExMzYuMzgsMTUuODQgOTA1Ljg4LDQxNS4xIDIwMTAuNTMsNDE1LjA5IiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNzFBQjIzIiBwb2ludHM9IjExMTYuMzgsMTUuODQgNjU1Ljk5LDE1Ljg0IDQ5NC4xNSwyOTYuMTcgNzI4LjM1LDY5NC44OCIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzhBQzkzNCIgcG9pbnRzPSI0ODQuMTUsMzA2LjE3IDI1NS4wNiw3MDIuOTYgMzg3LjY2LDkzMi42NCA4NDUuODMsOTMyLjYzIiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNThEMEZGIiBwb2ludHM9Ii03LjE3LDE0NDAuMDkgMTA5Ny45NywxNDQwLjA4IDEzMjguNDcsMTA0MC44MyAyMjMuMzIsMTA0MC44NSIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzEzQURGMyIgcG9pbnRzPSIxNzM5LjA0LDExNjAuOTEgMTUwOS4wOSw3NjIuNjQgMTExNy45NywxNDQwLjA4IDExODYuOTMsMTQ0MC4wOCAxNTc3Ljg3LDE0NDAuMDgiIC8+DQogIDxwb2x5Z29uIGZpbGw9IiMwMzkzRDAiIHBvaW50cz0iMTk3OC44LDc1Mi45NiAxODQ2LjIsNTIzLjMgMTM4Ni42OCw1MjMuMyAxNzQ5LjA0LDExNTAuOTEiIC8+DQo8L3N2Zz4=)](https://github.com/pjazdzyk/brent-dekker-solver) &nbsp;
[![Hvac-Engine](https://img.shields.io/badge/Hvac_Engine-2.2.0-13ADF3?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMi41bW0iIGhlaWdodD0iMTQuNW1tIiB2aWV3Qm94PSIwIDAgMjI1MCAxNDUwIj4NCiAgPHBvbHlnb24gZmlsbD0iIzUwN0QxNCIgcG9pbnRzPSIyMjQxLjAzLDE1Ljg4IDExMzYuMzgsMTUuODQgOTA1Ljg4LDQxNS4xIDIwMTAuNTMsNDE1LjA5IiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNzFBQjIzIiBwb2ludHM9IjExMTYuMzgsMTUuODQgNjU1Ljk5LDE1Ljg0IDQ5NC4xNSwyOTYuMTcgNzI4LjM1LDY5NC44OCIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzhBQzkzNCIgcG9pbnRzPSI0ODQuMTUsMzA2LjE3IDI1NS4wNiw3MDIuOTYgMzg3LjY2LDkzMi42NCA4NDUuODMsOTMyLjYzIiAvPg0KICA8cG9seWdvbiBmaWxsPSIjNThEMEZGIiBwb2ludHM9Ii03LjE3LDE0NDAuMDkgMTA5Ny45NywxNDQwLjA4IDEzMjguNDcsMTA0MC44MyAyMjMuMzIsMTA0MC44NSIgLz4NCiAgPHBvbHlnb24gZmlsbD0iIzEzQURGMyIgcG9pbnRzPSIxNzM5LjA0LDExNjAuOTEgMTUwOS4wOSw3NjIuNjQgMTExNy45NywxNDQwLjA4IDExODYuOTMsMTQ0MC4wOCAxNTc3Ljg3LDE0NDAuMDgiIC8+DQogIDxwb2x5Z29uIGZpbGw9IiMwMzkzRDAiIHBvaW50cz0iMTk3OC44LDc1Mi45NiAxODQ2LjIsNTIzLjMgMTM4Ni42OCw1MjMuMyAxNzQ5LjA0LDExNTAuOTEiIC8+DQo8L3N2Zz4=)](https://github.com/pjazdzyk/hvac-engine) &nbsp;

## 2. SYSTEM DESIGN
EnergyFlowX is designed as a small microservice deployed on an external server using docker swarm. Separation of Concerns is applied,
and the following independent services have been developed:

- **user manager service** - responsible for handling all user-related functions such as registration or account management,
- **business logic service** - HVAC process and fluid properties computation and units of measure conversion and all other features,
- **reverse proxy server** - Apache NGINX server instance, serving static frontend assets and acting as reverse proxy.

**Backend** service responsible for business logic was developed in hexagonal architecture. Why hexagonal? For practice and training, 
and because I like it. User manager was designed using classic multi-layer architecture.
Both services are designed as modular with separated API and CORE Maven modules. API module is composed of port interfaces to be implemented
by Rest Controllers in CORE infrastructure.<br>

**Frontend** is developed using the latest version of VUE.JS and Quasar, using JavaScript as a main programming language. Plenty of custom-made
components are designed to create ScientificInput acting as a placeholder for physical quantity value and unit with automatic validation
and value conversion when different unit is selected by user. <br>
Frontend is build to be **super lightweight and fast**. There is no single PNG or JPG image used on page. Only vector graphic is used
in SVG format including the icons. Pages are focused to deliver content, to be user-friendly, and to use the available screen size as much
as possible to fill it with relevant content without unnecessary distraction. After all this project is meant to be used by engineers in their daily routine. <br>

**Google Analytics** is used for basic page usage statistics. Proper **SEO** tags have been defined to ensure search engine positioning.

**Security** has been guaranteed following the best industry practices:

- RBAC (role-based access) provided to allow only a certain group of users to access specific content, leaving some content available for everyone,
- RODO / GDPR best practices are followed, application gathers as little data as possible respecting user privacy,
- HTTPS protocol in full/strict protocol used for all pages,
- state-of-art encryption algorithms are used to protect sensitive data,
- secrets are stored in an external cloud key-vault

## 3. CURRENT VERSION
Status: pre-release <br>
Version: **0.0.1-alpha**

## 4. FUNCTIONALITY

### ⇒ Available application capabilities:

**Dry air properties:**
* relative humidity,
* kinematic and dynamic viscosity,
* thermal conductivity,
* specific enthalpy,
* specific heat,
* density,
* thermal diffusivity,
* Prandtl number,

**Moist air properties:**
* vapour saturation pressure,
* dew point temperature, wet bulb temperature,
* relative humidity,
* humidity ratio and maximum humidity ratio,
* kinematic and dynamic viscosity,
* thermal conductivity,
* specific enthalpy of humid air with water mist and ice mist components,
* specific heat,
* density,
* thermal diffusivity,
* Prandtl number,

**Air heating:**
* heating process for input heating power,
* heating process for target outlet air temperature,
* heating process for target outlet air relative humidity,

**Air cooling:**
* real cooling process with a condensate discharge process for input cooling power,
* real cooling process with a condensate discharge process for target outlet temperature,
* real cooling process with a condensate discharge process for target outlet relative humidity,

**Air stream mixing:**
* simple mixing of two flows with humidity content,
* mixing of multiple flows with humidity content,

### ⇒ Functionalities available in the backend but not yet provided in the frontend:

**Sequential process computation procedure:**
* user defined collection of process definitions to be sequentially calculated using predecessor output as successor input, allowing to simulate any user custom HVAC process

**Hydraulic Conduits:**
* multiple shapes: circular, rectangular, elliptical
* flow velocity and Reynolds Number,
* Linear pressure loss and Linear resistance
* Colebrooke-White Friction Factor (numerical computation)
* Linear mass density of a duct, based on selected construction materials and insulation layers

## 5. REST API

REST Api is dedicated for developers who would like to use the capabilities of this service for developing
their own HVAC software systems. API DEMO version is available for free with limited functionality and heavy rate limiters applied: https://demo.energyflowx.com/.
Demo is provided for testing only. If you would like to have access to unlimited API - contact me for a custom pricing offer.

### 5.1. Versioning
Versioning is not planned for simplicity and to avoid maintaining of multiple apis and versions at the same time. However, if
you need it for any reason, please let me know.

### 5.2. Physical quantities master data

This endpoint provides information about all supported physical quantities and their corresponding units. It allows you to retrieve the full list of supported quantities and units, which can be useful for building dynamic interfaces or validating input data.

| LP | PATH                          | MTHD | PATH VARIABLE                     |
|----|-------------------------------|------|-----------------------------------|
| 1  | `/quantities`                 | GET  | None                              |
| 2  | `/quantities/{quantity-type}` | GET  | **quantity-type** (path variable) |

Example response for `/quantities/temperature`: [Quantities_masterdata_response](assets/json/quantities_masterdata_response.json) <br>

### 5.3. Physical quantities conversion

This service enables the conversion of any supported physical quantity from its current unit to a specified target unit, provided the target unit belongs to the same type of quantity. You can retrieve the full list of supported physical quantities and their corresponding units from the `/quantities` (master data) REST service.

| LP | PATH                                  | MTHD | QUERY PARAMS / REQUEST BODY                                                           |
|----|---------------------------------------|------|---------------------------------------------------------------------------------------|
| 1  | `/quantities/convert/{quantity-type}` | GET  | **quantity-type** (path variable)<br/>**value**<br/>**from-unit**<br/>**target-unit** |
| 2  | `/quantities/convert`                 | POST | [request-body-example](assets/json/multiple_quantity_conversion.json)                 |

Example response for multiple conversions: [Conversion_response](assets/json/conversion_response.json) <br>

### 5.4. Physical properties of humid air

Endpoints available for users are listed below. Parameters written in bold font are required, the rest are optional. If not
specified - default values will be assumed: <br>
- pressure: "101325.0Pa"
- relative-humidity: "0.0%"
- humidity ratio: "0.0kg/kg"
- imperial-units: "false"

Physical quantities must be specified as a String type with value and associated quantity unit, for example, "20.5C"
as 20.5 degrees of Celsius. For the list of supported units, see the [Unitility](https://github.com/pjazdzyk/unitility) user guide. <br>
Imperial units determine the unit system used in the response. For the input in query param or request objects, you can use
any unit you want from the supported units pool (both imperial and SI).

| LP | PATH                                   | MTHD | QUERY PARAMS                                                                                                |
|----|----------------------------------------|------|-------------------------------------------------------------------------------------------------------------|
| 1  | `/properties/dry-air`                  | GET  | **temperature**<br/>pressure<br/>imperial-units<br/>unit-overrides                                          |
| 2  | `/properties/humid-air`                | GET  | **temperature**<br/>pressure<br/>humidity-ratio<br/>relative-humidity<br/>imperial-units<br/>unit-overrides |
| 3  | `/properties/humid-air/from-wet-bulb`  | GET  | **wet-bulb-temperature**<br/>pressure<br/>relative-humidity<br/>imperial-units<br/>unit-overrides           |
| 4  | `/properties/humid-air/from-dew-point` | GET  | **dew-point-temperature**<br/>pressure<br/>relative-humidity<br/>imperial-units<br/>unit-overrides          |
| 5  | `/properties/humid-air/from-enthalpy`  | GET  | **specific-enthalpy**<br/>pressure<br/>**humidity-ratio**<br/>imperial-units<br/>unit-overrides             |
| 6  | `/properties/humid-air/from-humidity`  | GET  | **humidity-ratio**<br/>**relative-humidity**<br/>pressure<br/>imperial-units<br/>unit-overrides             |

Humid air response example: [Humid_air_response_SI](assets/json/humid_air_response.json) <br>

### 5.5. Process of heating
The process of heating is available in three different modes: from input power, for target temperature, or for target relative humidity.
More details on a heating process can be found in [HVAC|Engine](https://github.com/pjazdzyk/hvac-engine/blob/master/README_GUIDE.MD)
library user guide, section 3.1 Heating.

| LP | PATH                                          | MTHD | REQUEST BODY EXAMPLE                                             | QUERY PARAMS   |
|----|-----------------------------------------------|------|------------------------------------------------------------------|----------------|
| 1  | `/processes/heating/target-input-power`       | POST | [request-body-example](assets/json/heating_req_input_power.json) | imperial-units |
| 2  | `/processes/heating/target-temperature`       | POST | [request-body-example](assets/json/heating_req_target_temp.json) | imperial-units |
| 3  | `/processes/heating/target-relative-humidity` | POST | [request-body-example](assets/json/heating_req_target_RH.json)   | imperial-units |

As previously explained, setting query param imperial-units to true will provide a calculation result in a predefined set
of imperial units.<br>
Heating response example: [Heating_response_SI](assets/json/heating_response_temperature.json) <br>

### 5.6. Process of real cooling with condensate discharge
The process of cooling is available in three different modes: from input power, for target temperature, or for target relative humidity.
More details on a heating process can be found in [HVAC|Engine](https://github.com/pjazdzyk/hvac-engine/blob/master/README_GUIDE.MD)
library user guide, section 3.2 Cooling.

| LP | PATH                                          | MTHD | REQUEST BODY EXAMPLE                                             | QUERY PARAMS   |
|----|-----------------------------------------------|------|------------------------------------------------------------------|----------------|
| 1  | `/processes/cooling/target-input-power`       | POST | [request-body-example](assets/json/cooling_req_input_power.json) | imperial-units |
| 2  | `/processes/cooling/target-temperature`       | POST | [request-body-example](assets/json/cooling_req_target_temp.json) | imperial-units |
| 3  | `/processes/cooling/target-relative-humidity` | POST | [request-body-example](assets/json/cooling_req_target_RH.json)   | imperial-units |

Cooling response example: [Cooling_response_SI](assets/json/cooling_response_temperature.json) <br>

### 5.7. Process of mixing
The process of mixing is available in two different modes: mixing of two humid air flows and mixing of multiple humid air flows, up to 20.
More details on a heating process can be found in [HVAC|Engine](https://github.com/pjazdzyk/hvac-engine/blob/master/README_GUIDE.MD)
library user guide, section 3.3 Mixing.

| LP | PATH                         | MTHD | REQUEST BODY EXAMPLE                                    | QUERY PARAMS   |
|----|------------------------------|------|---------------------------------------------------------|----------------|
| 1  | `/processes/mixing`          | POST | [request-body-example](assets/json/mixing_request.json) | imperial-units |
| 2  | `/processes/mixing/multiple` | POST | [request-body-example](assets/json/mixing_request.json) | imperial-units |

Mixing response example: [Mixing_response_SI](assets/json/mixing_response.json) <br>

### 5.8. Sequential process computation
Sequential processing procedure allows specifying multiple connected processes to simulate real HVAC air handling units
or other devices. User specifies inlet airflow and process definitions (up to 20). Output of each process is taken
as input of another process next in line. Calculations are based on sequential processing engine and flow data connectivity 
model developed in HVAC|Engine library.

| LP | PATH                     | MTHD | REQUEST BODY EXAMPLE                                        | QUERY PARAMS   |
|----|--------------------------|------|-------------------------------------------------------------|----------------|
| 1  | `/procedures/sequential` | POST | [request-body-example](assets/json/sequential_request.json) | imperial-units |

Sequential procedure response example in SI units: [Multiple_processes_response_SI](assets/json/sequential_response.json) <br>

### 5.9. Unit Overrides
Unit Overrides allow you to specify in which unit a given quantity type should be provided in the response. 
This feature gives you flexibility to receive data in the units that are most convenient for your application or analysis.

Unit Overrides can be specified in two ways:
1. As part of the request body in JSON requests (in the `unitOverrides` field)
2. As query parameters for GET requests (using the `unit-overrides` parameter)

The `unitOverrides` object is a key-value map where:
- The key is the quantity type (e.g., "pressure", "temperature", "volumetricFlow")
- The value is the unit symbol you want to use (e.g., "kPa", "K", "m3/min")

Example of unit overrides in a request body:
```json
{
  "unitOverrides": {
    "pressure": "kPa",
    "temperature": "K",
    "volumetricFlow": "m3/min"
  }
}
```

Example of unit overrides as query parameters:
```
?unit-overrides=pressure_kPa,temperature_K
```

You can retrieve the full list of supported physical quantities and their corresponding units from the `/quantities` (master data) REST service.

### 5.10. Hydraulic Conduit
The Hydraulic Conduit API allows you to calculate flow parameters for different conduit shapes including circular, rectangular, and elliptical. It provides detailed information about flow characteristics, pressure losses, and conduit properties.

| LP | PATH                      | MTHD | REQUEST BODY EXAMPLE                                     | QUERY PARAMS   |
|----|---------------------------|------|----------------------------------------------------------|----------------|
| 1  | `/processes/conduit-flow` | POST | [request-body-example](assets/json/conduit_request.json) | imperial-units |

Conduit response example: [Conduit_response_SI](assets/json/conduit_response.json)

### 5.11. Error response
In case of validation errors or domain exceptions response will result in HTTP code of 400 (Bad Request).
[InvalidResponse](assets/json/error_response.json) will
be created and returned to user, with the following structure:
```json
{
   "serviceName": "Energy Flow X",
   "cause": "UnitSystemParseException",
   "message": "Unsupported unit symbol: {xyz}. Target class: TemperatureUnits",
   "timestamp": "2024-02-10T14:39:11.8551038Z"
}
```
Exception stack trace should never be returned to the user. If this happens, please let me know as soon as possible.

### 5.12. Swagger Ui
For easier API testing a SWAGGER UI has been provided, follow this URL: https://demo.energyflowx.com

## 6. LICENSING, ATTRIBUTION, AND CITATION
Please be informed that any reference to this project must be appropriately cited to include the author's attribution.
Additionally, it should be noted that while samples may have been shared publicly for educational purposes, the project
as a whole is designated for commercial utilization. Unauthorized commercial usage is strictly prohibited.
The author reserves all rights.

## 7. Feature request and bug reporting
I really appreciate your feedback and new ideas. This project was created by an engineer, for engineers.
I want this site to be as helpful as possible in your daily tasks. Please report any bugs or feature requests 
on the [GitHub Issues](https://github.com/pjazdzyk/energy-flow-x-demo/issues) page.

### **Help me improve by reporting any bugs you encounter.**
To ensure we can resolve issues quickly, please include the following information in your report:

- **Page or Functionality**: Specify which page or feature you were using when the issue occurred.
- **Description**: Provide a clear and detailed description of the bug.
- **Input Data**: Mention the data or inputs used when the bug occurred.
- **Result and Expectation**: Explain what happened and what you expected to happen.
- **App Version**: Include the app version, which you can find at the bottom of the application.

**Your feedback is the fuel that drives this project forward.**  
Every suggestion, idea, or bug report helps make this tool better for everyone—thank you for being a part of that process!

## 8. ACKNOWLEDGMENTS

I want to thank [Mabas83](https://github.com/mabas83), for everything you did for me. <br>
I extend my heartfelt gratitude to the [Silesian University of Technology](https://www.polsl.pl/en/) for the knowledge, scientific guidance, and for shaping me into an engineer.<br>
Special thanks for [GreedyJ4ck](https://github.com/greedyj4ck) for multiple discussion and valuable suggestions during frontend development. BIG THANKS!

## 9. REFERENCE SOURCES

* [1] - ASHRAE FUNDAMENTALS 2002, CHAPTER 6 "Psychrometrics"
* [2] - Buck, Arden L. "New Equations for Computing Vapour Pressure and Enhancement Factor". Journal of Applied Meteorology and Climatology (December 1981).
* [3] - Buck Research Instruments L.L.C. "MODEL CR-1A HYGROMETER WITH AUTO FILL OPERATING MANUAL" (May 2012).
* [4] - Morvay Z.K, Gvozdenac D.D. "Fundamentals for analysis and calculation of energy and environmental performance". Applied Industrial Energy And Environmental Management.
* [5] - Lipska B. "Projektowanie Wentylacji i Klimatyzacji. Podstawy uzdatniania powietrza" Wydawnictwo Politechniki Śląskiej (Gliwice 2014).
* [6] - https://www.engineeringtoolbox.com
* [7] - Stull R. "Wet-Bulb Temperature from Relative Humidity and Air Temperature". Manuscript received 14 July 2011, in final form 28 August 2011
* [8] - Tsilingiris P.T "Thermophysical and transport properties of humid air at temperature range between 0 and 100oC". Elsevier, Science Direct (September 2007)
* [9] - E.W. Lemmon, R.T. Jacobsen, S.G. Penoncello, D. Friend. Thermodynamic Properties of Air and Mixtures of Nitrogen, Argon, and Oxygen from 60 to 2000 K at Pressures to 2000 MPa. J. Phys. Chem. Ref. Data, Vol. 29, No. 3, (2000)
* [11] - F.E. Jones, G.L. Harris. ITS-90 Density of water formulation for volumetric standards' calibration. Journal of Research of the National Institute of Standards and Technology (1992)
* [12] - Water specific heat tables: https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html
* [13] - Mitosek M. Mechanika płynów w inżynierii i ochronie środowiska. Polskie Wydawnictwo Naukowe PWN (2001r).
* [14] - Lotfi Z., Jean Loup R., Bachir A. Explicit solutions for a turbulent flow friction factor: A review, assessment, and approaches classification. Ain Shams Engineering Journal (2019r)
* [15] - Brent-Dekker Iterative Solver - Modified Algorithm proposed by Zhengqiu Zhang / International Journal of Experimental Algorithms (IJEA), Volume (2) : Issue (1) : 2011
* [16] - F.E. Jones, G.L. Harris. ITS-90 Density of water formulation for volumetric standards' calibration. Journal of Research of the National Institute of Standards and Technology (1992)
* [17] - Water specific heat tables: https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html
* [18] - Antoine Equation Coefficient for pure substances: https://myengineeringtools.com/Data_Diagrams/Antoine_Law_Coefficients.html
* [19] - M. L. Huber,a… R. A. Perkins, A. Laesecke, and D. G. Friend. J. V. Sengers M. J. Assael and I. N. Metaxa E. Vogel R. Mareš K. Miyagawa. New International Formulation for the Viscosity of H2O. Journal of Research of the National Institute of Standards and Technology (1992)