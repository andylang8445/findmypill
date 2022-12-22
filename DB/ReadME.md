# Outline
## DB Backup
Shows the structure of each MariaDB Tables' structures
### Pill Specification
This table contains basic information about each pill themselves
<b>Categorization | Description </b>
--- | ---
id | Unique ID code for each pill
name | Name (or branding) of each pill
type | Type (or form) of the pill
company | Company produces each pill
consume | How to consume the pill
DIN | Unique DIN code for each pill, given by Canadian Governmant.<br>Multiple pills can have identical DIN codes in special cases.<br>Refer to [this page](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/applications-submissions/guidance-documents/regulatory-requirements-drug-identification-numbers/document.html) for more information

#### Sample Table
id | name | type | company | consume | DIN
--- | --- | --- | --- | --- | ---
1 | EXTRA STRENGTH TYLENOL COLD DAYTIME | Tablet | JOHNSON & JOHNSON INC | Oral | 2276186


### Pill Info
This table containes informations linking each ingredients and pills as well as their amounts<br>
i.e. <i>Which pill</i> contains <i>Which Ingredient</i> by <i>How Much</i>
<b>Categorization | Description </b>
--- | ---
id | ID of each pill that the row is referring to
Material_Info | Unique Ingredient code that each row is referring to
amount | how much ingredient is included in the pill<br>The unit of the amount is always seperated by a single space

#### Sample Table
id | Material_Info | amount
--- | --- | --- 
1 | 1 | 500 mg 
1 | 2 | 10 mg 
1 | 3 | 5 mg


### Material_Info
This table links each ingredient code with their name
<b>Categorization | Description </b>
--- | ---
id | ID of each ingredient
name | The name of each ingredient

#### Sample Table
id | name
--- | ---
1 | ACETAMINOPHEN
2 | DEXTROMETHORPHAN HYDROBROMIDE
3 | PHENYLEPHRINE HYDROCHLORIDE

## allfiles
Source: https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database/what-data-extract-drug-product-database.html
Description: Canadian Data
