# TKBL (Technologies Knowledge Base Library)

TKBL is a library that leverages advanced building-related projects from [ESTCP](https://serdp-estcp.mil/) and provides links to those reports. It also provides specific links to [SFTool.gov](https://sftool.gov/greenprocurement/federal#categories) and the Green Procurement Compilation product search tool.

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
```
# Import the function
from tkbl import filter_by_uniformat_code

# Test the function with a uniformat code
result = filter_by_uniformat_code('B202001')
print(result)
```

## Uniformat Code Mapping

TKBL supports searching for building-related projects and products by specific Uniformat codes. Below is a list of the categories and their corresponding Uniformat codes currently mapped within the library:

- **Domestic Water Equipment**: `D202003`
- **Compressed Air System (Non-Breathing)**: `D209005`
- **Other Special Plumbing Systems**: `D209090`
- **Oil Supply System**: `D301001`
- **Gas Supply System**: `D301002`
- **Steam Supply System (From Central Plant)**: `D301003`
- **Solar Energy Supply Systems**: `D301005`
- **Wind Energy Supply System**: `D301006`
- **Other Energy Supply**: `D301090`
- **Boilers**: `D302001`
- **Furnaces**: `D302002`
- **Fuel-Fired Unit Heaters**: `D302003`
- **Auxiliary Equipment**: `D302004`
- **Other Heat Generating Systems**: `D302090`
- **Chilled Water Systems**: `D303001`
- **Direct Expansion Systems**: `D303002`
- **Air Distribution, Heating & Cooling**: `D304001`
- **Steam Distribution Systems**: `D304002`
- **Hot Water Distribution Systems**: `D304003`
- **Glycol Distribution Systems**: `D304005`
- **Chilled Water Distribution Systems**: `D304006`
- **Exhaust Systems**: `D304007`
- **Air Handling Units**: `D304008`
- **Other Distribution Systems**: `D304090`
- **Unit Ventilators**: `D305001`
- **Unit Heaters**: `D305002`
- **Fan Coil Units**: `D305003`
- **Fin Tube Radiation**: `D305004`
- **Electric Heating**: `D305005` (Note: Also listed under Other Controls Instrumentation as `D509005`)
- **Package Units**: `D305006`
- **Other Terminal & Package Units**: `D305090`
- **HVAC Controls**: `D306001`
- **Electronic Controls**: `D306002`
- **Pneumatic Controls**: `D306003`
- **Instrument Air Compressors**: `D306004`
- **Gas Purging Systems**: `D306005`
- **Other Controls Instrumentation**: `D306090`
- **Refrigeration Systems**: `D309002`
- **Lighting Equipment**: `D502002`
- **Emergency Lighting & Power**: `D509002`
- **Lightning Protection**: `D509004`
- **Energy Management Control System**: `D509006`

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
- 
## Tests

To ensure TKBL is functioning as expected, you can run a series of tests provided with the library. These tests validate the integration with external resources and the correct application of Uniformat codes for filtering. 

To run the tests, navigate to the library's root directory in your terminal and execute the following command:

```bash
python -m unittest .\tests\test_tkbl.py
