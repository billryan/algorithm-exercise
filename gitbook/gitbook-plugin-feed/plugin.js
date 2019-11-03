require([ 'gitbook' ], function (gitbook) {
  gitbook.events.bind('start', function (e, config) {
    gitbook.toolbar.createButton({
      icon: 'fa fa-feed',
      label: 'Feed',
      position: 'right',
      onClick: function () {
        window.open('feed.xml');
      }
    });
  });
});
