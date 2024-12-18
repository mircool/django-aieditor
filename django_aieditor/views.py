from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
import os
import uuid

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('file')
        if image:
            # 生成唯一文件名
            ext = os.path.splitext(image.name)[1]
            filename = f'{uuid.uuid4().hex}{ext}'
            
            # 保存文件
            path = default_storage.save(f'aieditor/images/{filename}', image)
            
            # 获取完整URL
            file_url = settings.MEDIA_URL + path
            
            return JsonResponse({
                'success': True,
                'url': file_url,
                'message': '上传成功'
            })
    
    return JsonResponse({
        'success': False,
        'message': '上传失败'
    }) 