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

        insertItem: function(item) {
            console.log(item);
            return $.ajax({
                type: "POST",
                url: "/question/",
                data: item
            }).then(function(result) {
                return result;
            });
        },

        updateItem: function(item) {
            console.log(item);
            //item.distractors = item.distractors.split(',');
            //console.log(item);
            return $.ajax({
                type: "PUT",
                url: "/question/" + item.id,
                data: item
            }).then(function(result) {
                return result;
            });
        },

        deleteItem: function(item) {
            console.log(item);
            return $.ajax({
                type: "DELETE",
                url: "/question/" + item.id,
                data: item
            });
        }

    };

    window.db = db;

}());
