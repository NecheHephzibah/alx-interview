#!/usr/bin/node
const helper = require('util');
const apiCall = helper.promisify(require('request'));
const queryId = process.argv[2];

async function fetchItemDetails (recordId) {
  try {
    if (!recordId) {
      throw new Error('Please provide a film ID');
    }

    const baseUrl = 'https://swapi-api.hbtn.io/api/films/' + recordId;
    let rawData = await (await apiCall(baseUrl)).body;
    rawData = JSON.parse(rawData);

    if (!rawData.characters) {
      throw new Error('Invalid film ID or no character data found');
    }

    const itemList = rawData.characters;
    for (let index = 0; index < itemList.length; index++) {
      const detailPath = itemList[index];
      let itemData = await (await apiCall(detailPath)).body;
      itemData = JSON.parse(itemData);
      console.log(itemData.name);
    }
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

fetchItemDetails(queryId);
