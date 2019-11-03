require(['gitbook', 'jQuery'], function (gitbook, $) {
  function updateToc(_config) {
    var $toc = $( '#toc' );

    if ( $toc.length > 0 ) {}

    return true;
  }

  gitbook.events.bind('start', function (e, config) {
    updateToc();
  });

  gitbook.events.bind('page.change', function () {
    updateToc();
  });
});
