class UserObjectOwnerMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
