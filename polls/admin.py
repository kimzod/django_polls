from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    # 질문항목에 바로 답변을 달 수 있게 inline 옵션을 설정한다
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 변수를 이용하여 각 항목들을 그룹화 하고 그룹의 이름까지 설정한다
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 퀘스천 메인화면에서 보여질 항목들 [질문][등록일][최근등록여부]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    # 답변 클래스 등록
    inlines = [ChoiceInline]
    # 관리화면의 오른쪽에 필터링을 건다. 기준은 등록일
    list_filter = ['pub_date']
    # 검색필드를 생성한다. 검색 기준은 [question_text]
    search_fields = ['question_text']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text']


