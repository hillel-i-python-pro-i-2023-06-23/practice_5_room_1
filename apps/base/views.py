from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="Welcome! This is Yevhen Yalovenko Django base project.",
            #
            title="Home Page",
        )

        return context


class AboutUsView(TemplateView):
    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            about="This is just base project, but we definitely sooner or later became bigger,"
                  " more comfortable. Just wait=)",
            #
            title="About us",
        )

        return context
