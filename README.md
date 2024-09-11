# TKBL (Technologies Knowledge Base Library)

TKBL is a library that leverages advanced building-related projects from [ESTCP](https://serdp-estcp.mil/) and provides links to those reports. It also provides specific links to [SFTool.gov](https://sftool.gov/greenprocurement/federal#categories), the Green Procurement Compilation product search tool and [BuildingSync EE Measures](https://github.com/retrofit-lab/ashrae-1836-rp-categorization).

## Functionality

- **ESTCP Project Repository**: TKBL provides access to a collection of advanced building-related projects funded by the Environmental Security Technology Certification Program (ESTCP). Explore these projects at [ESTCP's official website](https://serdp-estcp.mil/).

- **SFTool.gov Integration**: The library offers links to resources on SFTool.gov, including the Green Procurement Compilation (GPC) product search tool, enabling users to explore sustainable building practices and products. Find sustainable products and practices at [SFTool.gov Green Procurement](https://sftool.gov/greenprocurement/federal#categories).

- **Uniformat Code Searching**: Users can search the dataset based on Uniformat codes, retrieving specific entries related to equipment types of interest.

## Matching ESTCP Reports to Uniformat Codes

The TKBL library enhances the utility of ESTCP reports by categorizing them according to Uniformat codes. This categorization was achieved through a meticulous process that involved analyzing report keywords and searching each report's abstract for matches to Uniformat descriptions. By leveraging natural language processing (NLP) techniques and manual review, we ensured a high degree of accuracy in matching reports to relevant building categories. This method allows users to efficiently locate ESTCP reports that are most relevant to specific building elements or systems, streamlining research and application processes in sustainable building practices.

### How It Works

1. **Keyword Analysis**: Initially, keywords from ESTCP reports were extracted and compared against a list of predefined terms associated with each Uniformat code category.
2. **Abstract Searching**: Each report's abstract was then searched for occurrences of these terms, as well as for matches to the more detailed descriptions provided by the Uniformat codes.
3. **Manual Review and Verification**: To ensure accuracy, results from the automated matching process were manually reviewed and verified, allowing for adjustments based on context and relevance.

This approach ensures that TKBL users have access to a curated and accurately categorized collection of ESTCP reports, facilitating targeted research and application in the field of advanced building technologies.

## Installation

You can install TKBL using pip:

```bash
pip install tkbl
```

## Usage

```python
# Import the function
from tkbl import filter_by_uniformat_code

# Test the function with a uniformat code
result = filter_by_uniformat_code('B202001')
print(result)
```

## Uniformat Code Mapping

TKBL supports searching for building-related projects and products by specific Uniformat codes. Below is a list of the categories and their corresponding Uniformat codes currently mapped within the library:

| System                                   | Code                                                                            |
|------------------------------------------|---------------------------------------------------------------------------------|
| Domestic Water Equipment                 | `D202003`                                                                       |
| Compressed Air System (Non-Breathing)    | `D209005`                                                                       |
| Other Special Plumbing Systems           | `D209090`                                                                       |
| Oil Supply System                        | `D301001`                                                                       |
| Gas Supply System                        | `D301002`                                                                       |
| Steam Supply System (From Central Plant) | `D301003`                                                                       |
| Solar Energy Supply Systems              | `D301005`                                                                       |
| Wind Energy Supply System                | `D301006`                                                                       |
| Other Energy Supply                      | `D301090`                                                                       |
| Boilers                                  | `D302001`                                                                       |
| Furnaces                                 | `D302002`                                                                       |
| Fuel-Fired Unit Heaters                  | `D302003`                                                                       |
| Auxiliary Equipment                      | `D302004`                                                                       |
| Other Heat Generating Systems            | `D302090`                                                                       |
| Chilled Water Systems                    | `D303001`                                                                       |
| Direct Expansion Systems                 | `D303002`                                                                       |
| Air Distribution, Heating & Cooling      | `D304001`                                                                       |
| Steam Distribution Systems               | `D304002`                                                                       |
| Hot Water Distribution Systems           | `D304003`                                                                       |
| Glycol Distribution Systems              | `D304005`                                                                       |
| Chilled Water Distribution Systems       | `D304006`                                                                       |
| Exhaust Systems                          | `D304007`                                                                       |
| Air Handling Units                       | `D304008`                                                                       |
| Other Distribution Systems               | `D304090`                                                                       |
| Unit Ventilators                         | `D305001`                                                                       |
| Unit Heaters                             | `D305002`                                                                       |
| Fan Coil Units                           | `D305003`                                                                       |
| Fin Tube Radiation                       | `D305004`                                                                       |
| Electric Heating                         | `D305005` (Note: Also listed under Other Controls Instrumentation as `D509005`) |
| Package Units                            | `D305006`                                                                       |
| Other Terminal & Package Units           | `D305090`                                                                       |
| HVAC Controls                            | `D306001`                                                                       |
| Electronic Controls                      | `D306002`                                                                       |
| Pneumatic Controls                       | `D306003`                                                                       |
| Instrument Air Compressors               | `D306004`                                                                       |
| Gas Purging Systems                      | `D306005`                                                                       |
| Other Controls Instrumentation           | `D306090`                                                                       |
| Refrigeration Systems                    | `D309002`                                                                       |
| Lighting Equipment                       | `D502002`                                                                       |
| Emergency Lighting & Power               | `D509002`                                                                       |
| Lightning Protection                     | `D509004`                                                                       |
| Energy Management Control System         | `D509006`                                                                       |

This mapping allows users to precisely filter the dataset for information relevant to their specific needs, enhancing the utility of TKBL in supporting sustainable building practices and equipment selection.

## Updating Data Files

The TKBL library references two primary CSV files for its dataset:

- ESTCP Uniformat Codes: [ESTCP_uniformat.csv](https://github.com/brianlball/TKBL/blob/main/tkbl/data/ESTCP_uniformat.csv)
- SFTool Uniformat Codes: [SFTool_uniformat.csv](https://github.com/brianlball/TKBL/blob/main/tkbl/data/SFTool_uniformat.csv)

To add new entries or update existing ones, follow these steps:

1. **Clone the Repository**: First, clone the TKBL repository to your local machine.
2. **Modify the CSV Files**: Navigate to the `tkbl/data/` directory. Open either `ESTCP_uniformat.csv` or `SFTool_uniformat.csv` in a spreadsheet editor or a text editor. Add new rows with the relevant data for each new entry. Ensure that you follow the existing format for consistency.
3. **Save Your Changes**: After adding your new entries, save the changes to the CSV file.

### Updating the Library Version

Once you have updated the data files, you should increment the version of the library to reflect the changes:

1. **Update `setup.py`**: Open the `setup.py` file located at the root of the TKBL repository. Increment the version number in a way that follows semantic versioning (e.g., if the current version is 1.0.0, update it to 1.0.1 for minor changes or to 1.1.0 for more significant updates).
2. **Rebuild the Package**: Run the following command to rebuild the TKBL package:

    ```bash
    python setup.py sdist bdist_wheel
    ```

3. **Test Your Changes**: Before submitting your changes, run the library's test suite to ensure that your updates do not introduce any issues.

### Submitting Your Changes

After making your changes and verifying that everything works as expected, consider submitting a pull request to the TKBL repository with your updates. This allows the maintainers to review your contributions and integrate them into the official library.

## Contributing to TKBL

Contributions are essential for keeping TKBL up-to-date and useful. We encourage contributions and please adhere the following workflow for making changes:

### How to Contribute

1. **Clone the Repository**: Clone the TKBL repository to your local machine. This step requires you to have GitHub permissions set up for the repository. If you do not have access, please contact the repository maintainers.

    ```bash
    git clone https://github.com/brianlball/TKBL.git
    cd TKBL
    ```

2. **Create a New Branch**: Before making any changes, create a new branch for your work. This helps in managing changes and ensures the main branch remains stable.

    ```bash
    git checkout -b your-branch-name
    ```

3. **Make Your Changes**: Perform the necessary modifications in your branch. If you're adding new entries or updating the CSV files, ensure your changes are accurate and follow the existing data format.

    - For ESTCP Uniformat Codes, update: [ESTCP_uniformat.csv](https://github.com/brianlball/TKBL/blob/main/tkbl/data/ESTCP_uniformat.csv)
    - For SFTool Uniformat Codes, update: [SFTool_uniformat.csv](https://github.com/brianlball/TKBL/blob/main/tkbl/data/SFTool_uniformat.csv)

4. **Commit and Push Your Changes**: After making your modifications, commit them to your branch and push the branch to the repository.

    ```bash
    git add .
    git commit -m "A clear and concise description of your changes"
    git push origin your-branch-name
    ```

5. **Submit a Pull Request (PR)**: Go to the TKBL repository on GitHub, navigate to the "Pull Requests" section, and click on "New Pull Request". Choose your branch and provide a detailed description of your changes for review.

### Guidelines for Contributions

- **Adhere to Conventions**: Ensure your changes adhere to the existing conventions in the CSV files and the overall structure of the repository.
- **Test Your Changes**: If possible, test your changes to ensure they do not introduce any issues. Include information about your testing in the pull request.
- **Documentation**: Update any documentation as necessary to reflect your changes. This includes modifying the README if your changes add new features or require additional instructions for use.

### Review and Merge

- After submitting your pull request, it will be reviewed by the repository maintainers. You may receive feedback and requests for adjustments.
- Once approved, your contributions will be merged into the main branch, making them part of the TKBL library.

## Tests

To ensure TKBL is functioning as expected, you can run a series of tests provided with the library. These tests validate the integration with external resources and the correct application of Uniformat codes for filtering.

To run the tests, navigate to the library's root directory in your terminal and execute the following command:

```bash
python -m unittest .\tests\test_tkbl.py
```

## BuildingSync EEMs

|eem_id|cat_lev1                                                            |eem_name                                                                                      |uni_code_manual|lvl4_uni_code|FIELD6                                       |lvl4_uni_code alternative|
|------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------|-------------|---------------------------------------------|-------------------------|
|1237  |Advanced Metering Systems                                           |Install advanced metering systems                                                             |D5010          |D501002      |SERVICE ENTRANCE EQUIPMENT                   |                         |
|1238  |Advanced Metering Systems                                           |Clean and/or repair                                                                           |D5010          |D501002      |SERVICE ENTRANCE EQUIPMENT                   |                         |
|1239  |Advanced Metering Systems                                           |Implement training and/or documentation                                                       |D5010          |D501002      |SERVICE ENTRANCE EQUIPMENT                   |                         |
|1240  |Advanced Metering Systems                                           |Upgrade operating protocols, calibration, and/or sequencing                                   |D5010          |D501002      |SERVICE ENTRANCE EQUIPMENT                   |                         |
|1241  |Advanced Metering Systems                                           |Other                                                                                         |D5010          |D501002      |SERVICE ENTRANCE EQUIPMENT                   |                         |
|1242  |Boiler Plant Improvements                                           |Replace boiler                                                                                |D3020          |D302001      |BOILERS                                      |                         |
|1243  |Boiler Plant Improvements                                           |Replace burner                                                                                |D3020          |D302001      |BOILERS                                      |                         |
|1244  |Boiler Plant Improvements                                           |Decentralize boiler                                                                           |D3020          |D302001      |BOILERS                                      |                         |
|1245  |Boiler Plant Improvements                                           |Insulate boiler room                                                                          |D3020          |D302001      |BOILERS                                      |                         |
|1246  |Boiler Plant Improvements                                           |Add energy recovery                                                                           |D3020          |D302001      |BOILERS                                      |                         |
|1247  |Boiler Plant Improvements                                           |Convert gas-fired unit to boiler loop                                                         |D3020          |D302001      |BOILERS                                      |                         |
|1248  |Boiler Plant Improvements                                           |Convert system from steam to hot water                                                        |D3020          |D302001      |BOILERS                                      |                         |
|1249  |Boiler Plant Improvements                                           |Clean and/or repair                                                                           |D3020          |D302001      |BOILERS                                      |                         |
|1250  |Boiler Plant Improvements                                           |Implement training and/or documentation                                                       |D3020          |D302001      |BOILERS                                      |                         |
|1251  |Boiler Plant Improvements                                           |Upgrade operating protocols, calibration, and/or sequencing                                   |D3020          |D302001      |BOILERS                                      |                         |
|1252  |Boiler Plant Improvements                                           |Convert to Cleaner Fuels                                                                      |D3020          |D302001      |BOILERS                                      |                         |
|1253  |Boiler Plant Improvements                                           |Other                                                                                         |D3020          |D302001      |BOILERS                                      |                         |
|1254  |Building Automation Systems/Energy Management Control Systems (EMCS)|Add heat recovery                                                                             |D3060          |D306001      |HVAC CONTROLS                                |                         |
|1255  |Building Automation Systems/Energy Management Control Systems (EMCS)|Add or upgrade BAS/EMS/EMCS                                                                   |D3060          |D306002      |ELECTRONIC CONTROLS                          |                         |
|1256  |Building Automation Systems/Energy Management Control Systems (EMCS)|Add or upgrade controls                                                                       |D3060          |D306001      |HVAC CONTROLS                                |D306002                  |
|1257  |Building Automation Systems/Energy Management Control Systems (EMCS)|Convert pneumatic controls to DDC                                                             |D3060          |D306003      |PNEUMATIC CONTROLS                           |D306002                  |
|1258  |Building Automation Systems/Energy Management Control Systems (EMCS)|Upgrade operating protocols, calibration, and/or sequencing                                   |D3060          |D306090      |OTHER CONTROLS INSTRUMENTATION               |                         |
|1259  |Building Automation Systems/Energy Management Control Systems (EMCS)|Other                                                                                         |D3060          |D306090      |OTHER CONTROLS INSTRUMENTATION               |                         |
|1260  |Building Envelope Modifications                                     |Air seal envelope                                                                             |B2010          |B201003      |INSULATION & VAPOR RETARDER                  |B301003                  |
|1261  |Building Envelope Modifications                                     |Increase wall insulation                                                                      |B2010          |B201003      |INSULATION & VAPOR RETARDER                  |                         |
|1262  |Building Envelope Modifications                                     |Insulate thermal bypasses                                                                     |B2010          |B201003      |INSULATION & VAPOR RETARDER                  |                         |
|1263  |Building Envelope Modifications                                     |Increase ceiling insulation                                                                   |C3030          |C303090      |OTHER CEILING & CEILING FINISHES             |                         |
|1264  |Building Envelope Modifications                                     |Increase roof insulation                                                                      |B3010          |B301003      |ROOF IINSULATION & FILL                      |                         |
|1265  |Building Envelope Modifications                                     |Insulate attic hatch / stair box                                                              |C3030          |C303090      |OTHER CEILING & CEILING FINISHES             |                         |
|1266  |Building Envelope Modifications                                     |Add attic/knee wall insulation                                                                |B2010          |B201003      |INSULATION & VAPOR RETARDER                  |B301003                  |
|1267  |Building Envelope Modifications                                     |Install cool/green roof                                                                       |B3010          |B301003      |ROOF IINSULATION & FILL                      |                         |
|1268  |Building Envelope Modifications                                     |Add shading devices                                                                           |B2010          |B201011      |SUN CONTROL DEVICES                          |                         |
|1269  |Building Envelope Modifications                                     |Add window films                                                                              |B2020          |B202001      |WINDOWS                                      |                         |
|1270  |Building Envelope Modifications                                     |Install or replace solar screens                                                              |B2010          |B201005      |EXTERIOR LOUVERS & SCREENS                   |                         |
|1271  |Building Envelope Modifications                                     |Replace glazing                                                                               |B2020          |B202004      |EXTERIOR GLAZING                             |                         |
|1272  |Building Envelope Modifications                                     |Replace windows                                                                               |B2020          |B202001      |WINDOWS                                      |                         |
|1273  |Building Envelope Modifications                                     |Increase floor insulation                                                                     |B1010          |B101090      |OTHER FLOOR CONSTRUCTION                     |                         |
|1274  |Building Envelope Modifications                                     |Insulate foundation                                                                           |A1010          |A101090      |OTHER STANDARD FOUNDATIONS                   |                         |
|1278  |Chilled Water, Hot Water, and Steam Distribution Systems            |Add pipe insulation                                                                           |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1279  |Chilled Water, Hot Water, and Steam Distribution Systems            |Repair and/or replace steam traps                                                             |D3040          |D304002      |STEAM DISTRIBUTION SYSTEMS                   |                         |
|1280  |Chilled Water, Hot Water, and Steam Distribution Systems            |Retrofit and replace chiller plant pumping, piping, and controls                              |D3030          |D303001      |CHILLED WATER SYSTEMS                        |D304006                  |
|1281  |Chilled Water, Hot Water, and Steam Distribution Systems            |Repair or replace existing condensate return systems or install new condensate return systems |D3040          |D304002      |STEAM DISTRIBUTION SYSTEMS                   |                         |
|1282  |Chilled Water, Hot Water, and Steam Distribution Systems            |Add recirculating pumps                                                                       |D3040          |D304003      |HOT WATER DISTRIBUTION SYSTEMS               |D202003                  |
|1283  |Chilled Water, Hot Water, and Steam Distribution Systems            |Replace or upgrade water heater                                                               |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1284  |Chilled Water, Hot Water, and Steam Distribution Systems            |Add energy recovery                                                                           |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1285  |Chilled Water, Hot Water, and Steam Distribution Systems            |Install solar hot water system                                                                |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |D301005                  |
|1286  |Chilled Water, Hot Water, and Steam Distribution Systems            |Separate SHW from heating                                                                     |D3040          |D304003      |HOT WATER DISTRIBUTION SYSTEMS               |                         |
|1287  |Chilled Water, Hot Water, and Steam Distribution Systems            |Replace with higher efficiency pump                                                           |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1288  |Chilled Water, Hot Water, and Steam Distribution Systems            |Replace with variable speed pump                                                              |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1289  |Chilled Water, Hot Water, and Steam Distribution Systems            |Install or upgrade master venting                                                             |D3040          |D304002      |STEAM DISTRIBUTION SYSTEMS                   |                         |
|1290  |Chilled Water, Hot Water, and Steam Distribution Systems            |Replace steam traps with orifice plates                                                       |D3040          |D304002      |STEAM DISTRIBUTION SYSTEMS                   |                         |
|1291  |Chilled Water, Hot Water, and Steam Distribution Systems            |Install steam condensate heat recovery                                                        |D3040          |D304002      |STEAM DISTRIBUTION SYSTEMS                   |                         |
|1292  |Chilled Water, Hot Water, and Steam Distribution Systems            |Clean and/or repair                                                                           |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1293  |Chilled Water, Hot Water, and Steam Distribution Systems            |Implement training and/or documentation                                                       |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1294  |Chilled Water, Hot Water, and Steam Distribution Systems            |Upgrade operating protocols, calibration, and/or sequencing                                   |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1295  |Chilled Water, Hot Water, and Steam Distribution Systems            |Other                                                                                         |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1296  |Chiller Plant Improvements                                          |Add energy recovery                                                                           |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1297  |Chiller Plant Improvements                                          |Install VSD on electric centrifugal chillers                                                  |D3030          |D303001      |CHILLED WATER SYSTEMS                        |                         |
|1298  |Chiller Plant Improvements                                          |Replace chiller                                                                               |D3030          |D303001      |CHILLED WATER SYSTEMS                        |                         |
|1299  |Chiller Plant Improvements                                          |Install gas cooling                                                                           |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1300  |Chiller Plant Improvements                                          |Add or repair economizer cycle                                                                |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1301  |Chiller Plant Improvements                                          |Add or replace cooling tower                                                                  |D3030          |D303001      |CHILLED WATER SYSTEMS                        |                         |
|1302  |Chiller Plant Improvements                                          |Clean and/or repair                                                                           |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1303  |Chiller Plant Improvements                                          |Implement training and/or documentation                                                       |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1304  |Chiller Plant Improvements                                          |Upgrade operating protocols, calibration, and/or sequencing                                   |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1305  |Chiller Plant Improvements                                          |Other                                                                                         |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1306  |Conveyance Systems (e.g., Elevators)                                |Add elevator regenerative drives                                                              |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1307  |Conveyance Systems (e.g., Elevators)                                |Upgrade controls                                                                              |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1308  |Conveyance Systems (e.g., Elevators)                                |Upgrade motors                                                                                |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1309  |Conveyance Systems (e.g., Elevators)                                |Clean and/or repair                                                                           |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1310  |Conveyance Systems (e.g., Elevators)                                |Implement training and/or documentation                                                       |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1311  |Conveyance Systems (e.g., Elevators)                                |Upgrade operating protocols, calibration, and/or sequencing                                   |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1312  |Conveyance Systems (e.g., Elevators)                                |Other                                                                                         |D1010          |D101090      |OTHER VERTICAL TRANSPORTATION EQUIPMENT      |                         |
|1321  |Distributed Generation                                              |Install CHP/cogeneration systems                                                              |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1322  |Distributed Generation                                              |Install fuel cells                                                                            |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1323  |Distributed Generation                                              |Install microturbines                                                                         |D3010          |D301006      |WIND ENERGY SUPPLY SYSTEM                    |                         |
|1324  |Distributed Generation                                              |Convert fuels                                                                                 |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1325  |Distributed Generation                                              |Clean and/or repair                                                                           |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1326  |Distributed Generation                                              |Implement training and/or documentation                                                       |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1327  |Distributed Generation                                              |Upgrade operating protocols, calibration, and/or sequencing                                   |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1328  |Distributed Generation                                              |Other                                                                                         |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1329  |Electrical Peak Shaving/Load Shifting                               |Install thermal energy storage                                                                |D3090          |D309090      |OTHER SPECIAL MECHANICAL SYSTEMS             |                         |
|1330  |Electrical Peak Shaving/Load Shifting                               |Implement training and/or documentation                                                       |G4010          |G401003      |SWITCHES, CONTROLS & DEVICES                 |                         |
|1331  |Electrical Peak Shaving/Load Shifting                               |Upgrade operating protocols, calibration, and/or sequencing                                   |G4010          |G401003      |SWITCHES, CONTROLS & DEVICES                 |                         |
|1332  |Electrical Peak Shaving/Load Shifting                               |Other                                                                                         |G4010          |G401003      |SWITCHES, CONTROLS & DEVICES                 |                         |
|1333  |Energy Cost Reduction Through Rate Adjustments                      |Change to more favorable rate schedule                                                        |D5010          |D501090      |OTHER SERVICE AND DISTRIBUTION               |                         |
|1334  |Energy Cost Reduction Through Rate Adjustments                      |Energy cost reduction through rate adjustments - uncategorized                                |D5010          |D501090      |OTHER SERVICE AND DISTRIBUTION               |                         |
|1335  |Energy Cost Reduction Through Rate Adjustments                      |Energy service billing and meter auditing recommendations                                     |D5010          |D501090      |OTHER SERVICE AND DISTRIBUTION               |                         |
|1336  |Energy Cost Reduction Through Rate Adjustments                      |Change to lower energy cost supplier(s)                                                       |D5010          |D501090      |OTHER SERVICE AND DISTRIBUTION               |                         |
|1337  |Energy Cost Reduction Through Rate Adjustments                      |Other                                                                                         |D5010          |D501090      |OTHER SERVICE AND DISTRIBUTION               |                         |
|1338  |Energy/Utility Distribution Systems                                 |Implement power factor corrections                                                            |G4010          |G401090      |OTHER ELECTRIC TRANSMISSION & DISTRIBUTION   |                         |
|1339  |Energy/Utility Distribution Systems                                 |Implement power quality upgrades                                                              |G4010          |G401090      |OTHER ELECTRIC TRANSMISSION & DISTRIBUTION   |                         |
|1340  |Energy/Utility Distribution Systems                                 |Upgrade transformers                                                                          |G4010          |G401002      |TRANSFORMERS                                 |D501001                  |
|1341  |Energy/Utility Distribution Systems                                 |Install gas distribution systems                                                              |G3060          |G306006      |GAS DISTRIBUTION PIPING (NATURAL AND PROPANE)|G306009                  |
|1342  |Energy/Utility Distribution Systems                                 |Clean and/or repair                                                                           |G4010          |G401090      |OTHER ELECTRIC TRANSMISSION & DISTRIBUTION   |                         |
|1343  |Energy/Utility Distribution Systems                                 |Implement training and/or documentation                                                       |G4010          |G401090      |OTHER ELECTRIC TRANSMISSION & DISTRIBUTION   |                         |
|1344  |Energy/Utility Distribution Systems                                 |Upgrade operating protocols, calibration, and/or sequencing                                   |G4010          |G401003      |SWITCHES, CONTROLS & DEVICES                 |                         |
|1345  |Energy/Utility Distribution Systems                                 |Other                                                                                         |G4010          |G401090      |OTHER ELECTRIC TRANSMISSION & DISTRIBUTION   |G306090                  |
|1353  |Lighting Improvements                                               |Retrofit with CFLs                                                                            |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1354  |Lighting Improvements                                               |Retrofit with T-5                                                                             |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1355  |Lighting Improvements                                               |Retrofit with T-8                                                                             |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1356  |Lighting Improvements                                               |Install spectrally enhanced lighting                                                          |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1357  |Lighting Improvements                                               |Retrofit with fiber optic lighting technologies                                               |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1358  |Lighting Improvements                                               |Retrofit with light emitting diode technologies                                               |D5020          |D502002      |LIGHTING EQUIPMENT                           |                         |
|1359  |Lighting Improvements                                               |Add daylight controls                                                                         |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1360  |Lighting Improvements                                               |Add occupancy sensors                                                                         |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1361  |Lighting Improvements                                               |Install photocell control                                                                     |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1362  |Lighting Improvements                                               |Install timers                                                                                |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1363  |Lighting Improvements                                               |Replace diffusers                                                                             |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1364  |Lighting Improvements                                               |Upgrade exit signs to LED                                                                     |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1365  |Lighting Improvements                                               |Upgrade exterior lighting                                                                     |G4020          |G402001      |EXTERIOR LIGHTING FIXTURES & CONTROLS        |                         |
|1366  |Lighting Improvements                                               |Clean and/or repair                                                                           |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1367  |Lighting Improvements                                               |Implement training and/or documentation                                                       |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1368  |Lighting Improvements                                               |Upgrade operating protocols, calibration, and/or sequencing                                   |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1369  |Lighting Improvements                                               |Other                                                                                         |D5020          |D502090      |OTHER LIGHTING AND BRANCH WIRING             |                         |
|1370  |Electric Motors and Drives Other than Those for Conveyance Systems  |Add drive controls                                                                            |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1371  |Electric Motors and Drives Other than Those for Conveyance Systems  |Replace with higher efficiency                                                                |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1372  |Electric Motors and Drives Other than Those for Conveyance Systems  |Add VSD motor controller                                                                      |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1373  |Electric Motors and Drives Other than Those for Conveyance Systems  |Clean and/or repair                                                                           |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1374  |Electric Motors and Drives Other than Those for Conveyance Systems  |Implement training and/or documentation                                                       |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1375  |Electric Motors and Drives Other than Those for Conveyance Systems  |Upgrade operating protocols, calibration, and/or sequencing                                   |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1376  |Electric Motors and Drives Other than Those for Conveyance Systems  |Other                                                                                         |D5010          |D501006      |MOTOR CONTROL CENTERS                        |                         |
|1377  |Heating, Ventilating, and Air Conditioning                          |Replace or modify AHU                                                                         |D3040          |D304008      |AIR HANDLING UNITS                           |                         |
|1378  |Heating, Ventilating, and Air Conditioning                          |Improve distribution fans                                                                     |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1379  |Heating, Ventilating, and Air Conditioning                          |Improve ventilation fans                                                                      |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1380  |Heating, Ventilating, and Air Conditioning                          |Convert CV system to VAV system                                                               |D3040          |D304008      |AIR HANDLING UNITS                           |D305006                  |
|1381  |Heating, Ventilating, and Air Conditioning                          |Repair leaks / seal ducts                                                                     |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1382  |Heating, Ventilating, and Air Conditioning                          |Add duct insulation                                                                           |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1383  |Heating, Ventilating, and Air Conditioning                          |Balance ventilation/distribution system                                                       |D3040          |D304090      |OTHER DISTRIBUTION SYSTEMS                   |                         |
|1384  |Heating, Ventilating, and Air Conditioning                          |Repair or replace HVAC damper and controller                                                  |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1385  |Heating, Ventilating, and Air Conditioning                          |Replace burner                                                                                |D3020          |D302090      |OTHER HEAT GENERATING SYSTEMS                |                         |
|1386  |Heating, Ventilating, and Air Conditioning                          |Replace package units                                                                         |D3050          |D305006      |PACKAGE UNITS                                |                         |
|1387  |Heating, Ventilating, and Air Conditioning                          |Replace packaged terminal units                                                               |D3050          |D305006      |PACKAGE UNITS                                |                         |
|1388  |Heating, Ventilating, and Air Conditioning                          |Install passive solar heating                                                                 |D3020          |D302090      |OTHER HEAT GENERATING SYSTEMS                |D301005                  |
|1389  |Heating, Ventilating, and Air Conditioning                          |Replace AC and heating units with ground coupled heat pump systems                            |D3030          |D303002      |DIRECT EXPANSION SYSTEMS                     |D302090                  |
|1390  |Heating, Ventilating, and Air Conditioning                          |Add enhanced dehumidification                                                                 |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1391  |Heating, Ventilating, and Air Conditioning                          |Install solar ventilation preheating system                                                   |D3090          |D309090      |OTHER SPECIAL MECHANICAL SYSTEMS             |D301005                  |
|1392  |Heating, Ventilating, and Air Conditioning                          |Add or repair economizer                                                                      |D3090          |D309090      |OTHER SPECIAL MECHANICAL SYSTEMS             |                         |
|1393  |Heating, Ventilating, and Air Conditioning                          |Add energy recovery                                                                           |D3090          |D309090      |OTHER SPECIAL MECHANICAL SYSTEMS             |                         |
|1394  |Heating, Ventilating, and Air Conditioning                          |Add or replace cooling tower                                                                  |D3030          |D303001      |CHILLED WATER SYSTEMS                        |                         |
|1395  |Heating, Ventilating, and Air Conditioning                          |Install thermal destratification fans                                                         |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1396  |Heating, Ventilating, and Air Conditioning                          |Install demand control ventilation                                                            |D3060          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |D306001                  |
|1397  |Heating, Ventilating, and Air Conditioning                          |Install gas cooling                                                                           |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1398  |Heating, Ventilating, and Air Conditioning                          |Install air source heat pump                                                                  |D3050          |D305006      |PACKAGE UNITS                                |                         |
|1399  |Heating, Ventilating, and Air Conditioning                          |Install variable refrigerant flow system                                                      |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |D302090                  |
|1400  |Heating, Ventilating, and Air Conditioning                          |Capture and return condensate                                                                 |D3030          |D303090      |OTHER COOLING GENERATING SYSTEMS             |                         |
|1401  |Heating, Ventilating, and Air Conditioning                          |Install or Upgrade Master Venting                                                             |D3040          |D304001      |AIR DISTRIBUTION, HEATING & COOLING          |                         |
|1420  |Refrigeration                                                       |Replace ice/refrigeration equipment with high efficiency units                                |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1421  |Refrigeration                                                       |Replace air-cooled ice/refrigeration equipment                                                |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1422  |Refrigeration                                                       |Replace refrigerators                                                                         |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1423  |Refrigeration                                                       |Clean and/or repair                                                                           |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1424  |Refrigeration                                                       |Implement training and/or documentation                                                       |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1425  |Refrigeration                                                       |Upgrade operating protocols, calibration, and/or sequencing                                   |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1426  |Refrigeration                                                       |Other                                                                                         |D3090          |D309002      |REFRIGERATION SYSTEMS                        |                         |
|1427  |Renewable Energy Systems                                            |Install landfill gas, wastewater treatment plant digester gas, or coal bed methane power plant|D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1428  |Renewable Energy Systems                                            |Install photovoltaic system                                                                   |D3010          |D301005      |SOLAR ENERGY SUPPLY SYSTEMS                  |                         |
|1429  |Renewable Energy Systems                                            |Install wind energy system                                                                    |D3010          |D301006      |WIND ENERGY SUPPLY SYSTEM                    |                         |
|1430  |Renewable Energy Systems                                            |Install wood waste or other organic waste stream heating or power plant                       |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1431  |Renewable Energy Systems                                            |Clean and/or repair                                                                           |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1432  |Renewable Energy Systems                                            |Implement training and/or documentation                                                       |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1433  |Renewable Energy Systems                                            |Upgrade operating protocols, calibration, and/or sequencing                                   |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1434  |Renewable Energy Systems                                            |Other                                                                                         |D3010          |D301090      |OTHER ENERGY SUPPLY                          |                         |
|1435  |Service hot water (SHW) and domestic hot water (DHW) systems        |Decrease SHW temperature                                                                      |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |D304003                  |
|1436  |Service hot water (SHW) and domestic hot water (DHW) systems        |Install SHW controls                                                                          |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |D304003                  |
|1437  |Service hot water (SHW) and domestic hot water (DHW) systems        |Install solar thermal SHW                                                                     |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |D304003                  |
|1438  |Service hot water (SHW) and domestic hot water (DHW) systems        |Install water pressure booster                                                                |D2020          |D202005      |SPECIALTIES                                  |D304003                  |
|1439  |Service hot water (SHW) and domestic hot water (DHW) systems        |Insulate SHW piping                                                                           |D2020          |D202001      |PIPES & FITTINGS                             |D304003                  |
|1440  |Service hot water (SHW) and domestic hot water (DHW) systems        |Insulate SHW tank                                                                             |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1441  |Service hot water (SHW) and domestic hot water (DHW) systems        |Replace piping                                                                                |D2020          |D202001      |PIPES & FITTINGS                             |D304003                  |
|1442  |Service hot water (SHW) and domestic hot water (DHW) systems        |Replace tankless coil                                                                         |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1443  |Service hot water (SHW) and domestic hot water (DHW) systems        |Separate SHW from heating                                                                     |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1444  |Service hot water (SHW) and domestic hot water (DHW) systems        |Upgrade SHW boiler                                                                            |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1445  |Service hot water (SHW) and domestic hot water (DHW) systems        |Install heat pump SHW system                                                                  |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1446  |Service hot water (SHW) and domestic hot water (DHW) systems        |Install tankless water heaters                                                                |D2020          |D202003      |DOMESTIC WATER EQUIPMENT                     |D304003                  |
|1447  |Service hot water (SHW) and domestic hot water (DHW) systems        |Clean and/or repair                                                                           |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |                         |
|1448  |Service hot water (SHW) and domestic hot water (DHW) systems        |Implement training and/or documentation                                                       |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |                         |
|1449  |Service hot water (SHW) and domestic hot water (DHW) systems        |Upgrade operating protocols, calibration, and/or sequencing                                   |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |                         |
|1450  |Service hot water (SHW) and domestic hot water (DHW) systems        |Other                                                                                         |D2020          |D202090      |OTHER DOMESTIC WATER SUPPLY                  |                         |
|1452  |Water and Sewer Conservation Systems                                |Install low-flow faucets and showerheads                                                      |D2010          |D201001      |WATERCLOSETS                                 |D201005                  |
|1453  |Water and Sewer Conservation Systems                                |Install low-flow plumbing equipment                                                           |D2020          |D202005      |SPECIALTIES                                  |D209001                  |
|1454  |Water and Sewer Conservation Systems                                |Install onsite sewer treatment systems                                                        |G3020          |G302004      |PACKAGED SANITARY SEWER TREATMENT PLANTS     |D203004                  |
|1455  |Water and Sewer Conservation Systems                                |Implement water efficient irrigation                                                          |G2050          |G205007      |IRRIGATION SYSTEMS                           |                         |
|1459  |Water and Sewer Conservation Systems                                |Other                                                                                         |G3010          |G302090      |OTHER SANITARY SEWER                         |G301090                  |
