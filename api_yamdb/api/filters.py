from rest_framework import filters


class TitleFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category_slug = request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        genre_slug = request.query_params.get('genre', None)
        if genre_slug:
            queryset = queryset.filter(genre__slug=genre_slug)
        name = request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset
