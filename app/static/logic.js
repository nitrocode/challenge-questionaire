(function() {

    var db = {

        loadData: function(filter) {
            return $.ajax({
                type: "GET",
                url: "/questions",
                data: filter,
                dataType: "JSON"
            }).then(function(result) {
                d = result.data;
                // join distractors array or jsGrid will fail
                for (var i=0; i < d.length; i++) {
                    d[i].distractors = d[i].distractors.join();
                }
                return d;
            });
        },

        _method_function: function(item, type) {
            console.log(item);
            item.distractors = item.distractors.split(',');
            d = item.distractors;
            for (var i=0; i < d.length; i++)
                d[i] = parseInt(d[i]);
            console.log(item);
            return $.ajax({
                type: type,
                url: "/question/" + item.id,
                data: item
            }).then(function(result) {
                return result;
            });
        },

        insertItem: function(item) {
            this._method_function(item, 'POST');
        },

        updateItem: function(item) {
            this._method_function(item, 'PUT');
        },

        deleteItem: function(item) {
            this._method_function(item, 'DELETE');
        }

    };

    window.db = db;

}());
