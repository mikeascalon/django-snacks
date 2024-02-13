from django.views.generic import TemplateView  

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/225Fish_and_Taho_vendors_in_Bulacan_17.jpg",
                "title": "taho",
                "description": "Tahoo street vendors Taho with sago pearls ",
                "reference_url": "https://commons.wikimedia.org/wiki/File:225Fish_and_Taho_vendors_in_Bulacan_17.jpg"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/91/3395San_Antonio_Valley_Street_Foods_05.jpg",
                "title": "Turron",
                "description": "English: Carioca (food), Turron, Banana Cue, Camote Cue.",
                "reference_url": "https://commons.wikimedia.org/wiki/File:3395San_Antonio_Valley_Street_Foods_05.jpg"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/25/185Cuisine_food_of_Bulacan_43.jpg",
                "title": "Puto Kutsinta",
                "description": "Cuisine food of Bulacan Taken in Poblacion, Baliuag, Bulacan .",
                "reference_url": "https://commons.wikimedia.org/wiki/File:185Cuisine_food_of_Bulacan_43.jpg"
            },
        ]

        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    