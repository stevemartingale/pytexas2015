Toys = new Mongo.Collection("toys");

if (Meteor.isClient) {
    Handlebars.registerHelper('getColor', function(temp) {
        if (temp > 100) {
            return "label-danger";
        } else {
            return "label-success";
        }
    });

    Template.body.helpers({
        toys: function() {
            return Toys.find({}, {sort: { machineId: 1 }});
        }
    });
}

if (Meteor.isServer) {
    Meteor.startup(function() {
        // code to run on server at startup
    });
}
