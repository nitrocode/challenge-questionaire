(function() {

    var db = {
        /**
         * Enables updating an item by pressing enter.
         */
        editOnEnter: function(value) {
            // https://github.com/tabalinas/jsgrid/issues/243#issuecomment-205171378
            var $result = jsGrid.fields.number.prototype.editTemplate.call(this, value);
            $result.on("keydown", function(e) {
                if(e.which === 13) {
                    $("#grid").jsGrid("updateItem");
                    return false;
                }
            });
            return $result;
        },

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
            // in case an empty value was saved, then removed
            item.distractors = (typeof item.id === 'undefined') ? [] : item.distractors.split(',');
            d = item.distractors;
            for (var i=0; i < d.length; i++)
                d[i] = parseInt(d[i]);
            console.log(item);
            // if item id is empty i.e. adding a new question,
            // enter an empty id so Flask can set the item id
            item.id = (typeof item.id === 'undefined') ? "" : item.id;
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
