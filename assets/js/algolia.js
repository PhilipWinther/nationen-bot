// Instanciating InstantSearch.js with Algolia credentials
const search = instantsearch({
  appId: '3PRPCH5R4B',
  apiKey: '7d31032d9031dd20b055d3af08715558',
  indexName: 'philip-winther.dk',
  searchParameters: {
    restrictSearchableAttributes: [
      'title',
      'content',
      'categories',
      'tags'
    ]
  }
});

const hitTemplate = function(hit) {
  const url = hit.url;
  const title = hit._highlightResult.title.value;
  const content = hit._highlightResult.html.value;

  return `
    <div class="list__item">
      <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        <h2 class="archive__item-title" itemprop="headline"><a href="${url}">${title}</a></h2>
        <div class="archive__item-excerpt" itemprop="description">${content}</div>
      </article>
    </div>
  `;
}

// Adding searchbar and results widgets
search.addWidget(
  instantsearch.widgets.searchBox({
    container: '.search-searchbar',
    poweredBy: true,
    placeholder: 'Enter your search term...'
  })
);
search.addWidget(
  instantsearch.widgets.hits({
    container: '.search-hits',
    templates: {
      item: hitTemplate,
      empty: 'No results',
    }
  })
);

// Starting the search only when toggle is clicked
$(document).ready(function () {
  $(".search__toggle").on("click", function() {
    if(!search.started) {
      search.start();
    }
  });
});

